import boto3
import logging
import json
import logging.config
import requests
import config

from botocore.config import Config
from utils import entity, mqtt

logging.basicConfig(level=logging.INFO)
logging.getLogger('urllib3.util.retry').setLevel(logging.ERROR)
logging.getLogger('urllib3.connectionpool').setLevel(logging.ERROR)
logging.getLogger('botocore.auth').setLevel(logging.ERROR)
logging.getLogger('botocore.hooks').setLevel(logging.ERROR)
logging.getLogger('botocore.retryhandler').setLevel(logging.ERROR)
logging.getLogger('botocore.args').setLevel(logging.ERROR)
logging.getLogger('botocore.endpoint').setLevel(logging.ERROR)
logging.getLogger('botocore.client').setLevel(logging.ERROR)
logging.getLogger('botocore.loaders').setLevel(logging.ERROR)
logging.getLogger('botocore.parsers').setLevel(logging.ERROR)

client = boto3.resource(
    'sqs',
    region_name=config.AWS_REGION,
    aws_access_key_id=config.AWS_ACCESS_KEY,
    aws_secret_access_key=config.AWS_SECRET_KEY,
    config=Config(
        retries = {
            'max_attempts': 10,
            'mode': 'standard'
        }
    )
)

queue = client.Queue(config.SQS_QUEUE)

while(True):
    messages = queue.receive_messages(
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=20
    )

    for message in messages:
        try:
            message_body = json.loads(message.body)
        except ValueError as e:
            message_body = message.body

        message_data = {
            'body': message_body,
            'message_attributes': message.message_attributes
        }
        print(f"INFO: {message_data}")

        if message_data['body'] or message_data['message_attributes']:
            if config.ENTITY_ID:
                print(f"INFO: Update entity {config.ENTITY_ID}")
                entity.update_entity(
                    config.ENTITY_ID,
                    config.SUPERVISOR_API,
                    config.SUPERVISOR_TOKEN,
                    message_data
                )
            if config.MQTT_ENABLE:
                print(f"INFO: Push to mqtt topic {config.MQTT_TOPIC}")
                mqtt.mqtt_publish(
                    config.MQTT_HOST,
                    config.MQTT_USER,
                    config.MQTT_PASS,
                    config.MQTT_TOPIC,
                    json.dumps(message_data)
                )
        message.delete()