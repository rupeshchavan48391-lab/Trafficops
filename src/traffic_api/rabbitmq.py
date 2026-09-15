import json

import pika


RABBITMQ_HOST = "127.0.0.1"
RABBITMQ_PORT = 5672
RABBITMQ_USER = "trafficops"
RABBITMQ_PASSWORD = "trafficops"
QUEUE_NAME = "traffic_events"


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

    channel.queue_declare(queue=QUEUE_NAME)

    channel.basic_publish(
        exchange="",
        routing_key=QUEUE_NAME,
        body=json.dumps(event),
    )

    connection.close()
