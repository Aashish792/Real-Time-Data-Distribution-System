import pika
import sys
import time

# Configure your RabbitMQ connection parameters
rabbitmq_host = 'localhost'
queue_name = 'realtime_data'    

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")

def start_consumer():
    while True:
        try:
            # RabbitMQ connection
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
            channel = connection.channel()

            # Ensure this matches the existing queue's 'durable' property
            channel.queue_declare(queue=queue_name, durable=True)

            # Setup the consumption of messages from the 'realtime_data' queue
            channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()
        except pika.exceptions.ConnectionClosedByBroker:
            # Unlikely in this case, but it can happen if the broker closes the connection, e.g. due to misconfiguration.
            print("Connection was closed by broker, trying to reconnect...")
            continue
        except pika.exceptions.AMQPChannelError as err:
            print(f"Caught a channel error: {err}, stopping...")
            break
        except pika.exceptions.AMQPConnectionError:
            print("Connection was closed, retrying...")
            time.sleep(5)
            continue
        except KeyboardInterrupt:
            print("Consumer stopped by user.")
            try:
                if connection.is_open:
                    connection.close()
            except Exception as e:
                print(f"Failed to close connection on KeyboardInterrupt: {e}")
            sys.exit(0)

if __name__ == "__main__":
    start_consumer()
