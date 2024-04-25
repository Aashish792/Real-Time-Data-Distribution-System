# consumer_with_websocket.py
import pika
import websocket
import threading
import json

# Connect to the WebSocket server as a client
def start_websocket_client():
    def on_message(ws, message):
        print(f"Received from WebSocket: {message}")

    def on_error(ws, error):
        print(f"WebSocket error: {error}")

    def on_close(ws):
        print("WebSocket closed")

    ws = websocket.WebSocketApp("ws://localhost:8765",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()

def start_rabbitmq_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='realtime_data', durable=True)
    ws_client = websocket.create_connection("ws://localhost:8765")

    def callback(ch, method, properties, body):
        print(f"Received from RabbitMQ: {body.decode()}")
        # Send the message to the WebSocket server
        ws_client.send(body.decode())

    channel.basic_consume(queue='realtime_data', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

# Run the WebSocket client in a separate thread
threading.Thread(target=start_websocket_client, daemon=True).start()

# Run the RabbitMQ consumer in the main thread
start_rabbitmq_consumer()
