import boto3
import logging
import json
import logging.config
import requests
import config

from utils import entity

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
        if message.body:
            entity.update_entity(
                config.ENTITY_ID,
                config.SUPERVISOR_API,
                config.SUPERVISOR_TOKEN,
                json.loads(message.body)
            )
        message.delete()