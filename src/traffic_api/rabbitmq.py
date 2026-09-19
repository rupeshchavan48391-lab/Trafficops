import json
import os

import pika
from dotenv import load_dotenv


load_dotenv()


RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT"))
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
QUEUE_NAME = os.getenv("RABBITMQ_QUEUE")


def publish_event(event):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            credentials=pika.PlainCredentials(
                username=RABBITMQ_USER,
                password=RABBITMQ_PASSWORD,
            ),
        )
    )

    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME,durable=True)

    channel.basic_publish(
        exchange="",
        routing_key=QUEUE_NAME,
        body=json.dumps(event),
    )

    connection.close()
