from confluent_kafka import Producer

# Kafka broker address
bootstrap_servers = 'localhost:9092'

# Kafka topic to produce messages to
topic = 'my-topic'

# Create Kafka producer configuration
conf = {
    'bootstrap.servers': bootstrap_servers
}

# Create Kafka producer instance
producer = Producer(conf)

# Produce messages to Kafka topic
for i in range(10):
    message = f'Message {i+1}'
    producer.produce(topic, value=message.encode('utf-8'))
    print(f"Produced message: {message}")

# Flush any remaining messages in the producer buffer
producer.flush()
