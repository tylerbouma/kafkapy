from confluent_kafka import Consumer, KafkaError

# Configure Kafka consumer
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
    'group.id': 'my-consumer-group',  # Consumer group ID
    'auto.offset.reset': 'earliest'  # Start consuming from the beginning of the topic
}

# Create Kafka consumer instance
consumer = Consumer(conf)

# Subscribe to the Kafka topic
consumer.subscribe(['my-topic'])

# Start consuming messages
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                #End of partition, continue polling
                continue
            else:
                # Error occurred
                print(f"Error: {msg.error()}")
                break
        else:
            # Message received
            print(f"Received message: {msg.value().decode('utf-8')}")
            
except KeyboardInterrupt:
    pass

finally:
    consumer.close()
