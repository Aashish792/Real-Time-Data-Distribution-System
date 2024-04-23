import pika
import json

# Configure your RabbitMQ server connection here
rabbitmq_host = 'localhost'
queue_name = 'realtime_data'

def produce_message(data):
    try:
        # Setup the connection to RabbitMQ server
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
        channel = connection.channel()
        
        # Make sure the queue exists. If it does not, it will be created.
        channel.queue_declare(queue=queue_name, durable=True)  # 'durable' makes the queue survive broker restarts
        
        # Convert the message data to JSON format
        message = json.dumps(data)
        
        # Publish the message to the queue
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=message,
                              properties=pika.BasicProperties(
                                  delivery_mode=2,  # Make message persistent
                              ))
        print(f" [x] Sent data to queue '{queue_name}': {data}")
    except pika.exceptions.AMQPConnectionError as error:
        print(f"Failed to connect to RabbitMQ server: {error}")
    except pika.exceptions.AMQPChannelError as error:
        print(f"Channel error occurred: {error}")
    except Exception as error:
        print(f"An error occurred: {error}")
    finally:
        # Close the connection
        if 'connection' in locals() and connection.is_open:
            connection.close()

if __name__ == "__main__":
    # Simulating data production
    while True:
        data_input = input("Enter your message: ")
        produce_message(data_input)
