import time
from faker import Faker
from confluent_kafka import Producer
import json

fake = Faker()

bootstrap_servers = 'your-cluster-endpoint:9092'  
sasl_plain_username = 'your-api-key'
sasl_plain_password = 'your-api-secret'
topic_name = 'your-topic-name'

# Create the Kafka producer
producer_config = {
    'bootstrap.servers': bootstrap_servers,
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': sasl_plain_username,
    'sasl.password': sasl_plain_password,
}

producer = Producer(producer_config)


def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to topic {} [partition {}] at offset {}'.format(msg.topic(), msg.partition(), msg.offset()))


def get_registered_users():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "message": fake.text(),
        "created_on": fake.year()
    }

while True:
    user = get_registered_users()

    # Convert user data to JSON format
    user_json = json.dumps(user)

    # Produce the message to Kafka
    producer.produce(topic_name, user_json, callback=delivery_report)
    producer.flush()  # Ensure message is sent

    time.sleep(30)