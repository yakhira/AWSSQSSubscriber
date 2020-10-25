import json
import os

SUPERVISOR_TOKEN = os.getenv('SUPERVISOR_TOKEN')
HASSIO_TOKEN = os.getenv('HASSIO_TOKEN')
SUPERVISOR_API = 'http://supervisor/core/api'

SQS_QUEUE = os.getenv('SQS_QUEUE')
AWS_REGION = os.getenv('AWS_REGION')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
ENTITY_ID = os.getenv('ENTITY_ID')

MQTT_TOPIC = os.getenv('MQTT_TOPIC')
MQTT_HOST = os.getenv('MQTT_HOST')
MQTT_USER = os.getenv('MQTT_USER')
MQTT_PASS = os.getenv('MQTT_PASSWORD')

MQTT_ENABLE = True if MQTT_TOPIC and MQTT_HOST and MQTT_USER and MQTT_PASS else False