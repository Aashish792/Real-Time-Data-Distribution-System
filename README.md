Here's the updated README file with the enhanced WebSocket setup included, reflecting the latest changes to the scripts for better integration and functionality.

---

# Real-Time Data Distribution System

## Introduction

This project implements a real-time data distribution system leveraging advanced queue mechanisms and socket communication to ensure efficient and reliable data transfer across different network nodes. It is designed to be a proof-of-concept system that demonstrates the effectiveness of using queues (RabbitMQ) and sockets (WebSockets) in a distributed environment for real-time data delivery.

## System Overview

The system consists of three main components:

1. **Data Producer**: Generates and sends messages to the queue server.
2. **Queue Server (RabbitMQ)**: Manages message queues and ensures reliable message transfer.
3. **Data Consumer**: Retrieves messages from the queue server and can forward them to clients via WebSockets.

The system's architecture is designed for high availability and low latency, making it suitable for applications such as live streaming or real-time analytics.

## Technologies Used

- **RabbitMQ**: For message queuing between producers and consumers.
- **WebSockets**: For real-time communication between the server and clients.
- **Python**: For backend development, including both the producer and consumer scripts.

## Prerequisites

Before running this system, ensure that you have the following installed:

- Python 3.8 or higher
- RabbitMQ server
- Pika Python library (for interacting with RabbitMQ)
- Websockets Python library (for managing WebSocket connections)

## Setup Instructions

1. **Install RabbitMQ**: Follow the official instructions for your system to install and run the RabbitMQ server.

2. **Install Python Libraries**:
   ```
   pip install pika websocket-client websockets
   ```

3. **Clone the Repository**:
   ```
   git clone https://your-repository-url.git
   cd your-repository-directory
   ```

4. **Configure RabbitMQ** (optional): If you wish to change the default RabbitMQ connection settings, update the `rabbitmq_host` variable in both the producer and consumer scripts.

## Running the System

1. **Start the RabbitMQ Server**: Ensure the RabbitMQ service is running on your host machine.

2. **Run the WebSocket Server**:
   ```
   python websocket_server.py
   ```

3. **Run the Data Producer**:
   ```
   python producer.py
   ```
   This will prompt you to enter messages that will be sent to the queue.

4. **Run the Data Consumer with WebSocket Integration**:
   ```
   python consumer_with_websocket.py
   ```
   The consumer will listen to the queue and forward any messages it receives to the WebSocket server, which then broadcasts these messages to all connected clients.

## Scope

The current implementation is intended to serve as a starting point. It does not cover deployment in a production environment or detailed security measures, such as encryption of data in transit.

## Troubleshooting

- If the consumer or producer scripts fail to connect to RabbitMQ, verify that the RabbitMQ service is running and the connection parameters are correct.
- If there are issues with messages not appearing in the queue, check that the queue names match in both the producer and consumer scripts.
- Check the RabbitMQ management console to monitor queues and message flow.

