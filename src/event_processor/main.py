import json
import os

import pika
from dotenv import load_dotenv

from src.traffic_api.database import get_connection


load_dotenv()


RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT"))
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
QUEUE_NAME = os.getenv("RABBITMQ_QUEUE")


def store_event(event):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO traffic_events (
                    sensor_id,
                    road_id,
                    vehicle_count,
                    average_speed,
                    congestion_level,
                    timestamp
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    event["sensor_id"],
                    event["road_id"],
                    event["vehicle_count"],
                    event["average_speed"],
                    event["congestion_level"],
                    event["timestamp"],
                ),
            )

            event_id = cur.fetchone()[0]

    return event_id


def process_message(ch, method, properties, body):
    event = json.loads(body)

    print("Received traffic event:")
    print(event)

    event_id = store_event(event)

    print(f"Event stored in PostgreSQL with ID: {event_id}")

    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
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

    channel.queue_declare(
        queue=QUEUE_NAME,
        durable=True,
    )

    channel.basic_consume(
        queue=QUEUE_NAME,
        on_message_callback=process_message,
    )

    print("Event Processor started.")
    print("Waiting for traffic events...")

    channel.start_consuming()


if __name__ == "__main__":
    main()
