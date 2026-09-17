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
