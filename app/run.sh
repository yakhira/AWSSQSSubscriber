#!/usr/bin/with-contenv bashio
set +u

CONFIG_PATH=/data/options.json
SYSTEM_USER=/data/system_user.json

export SQS_QUEUE=$(jq --raw-output ".sqs_queue" $CONFIG_PATH)
export AWS_REGION=$(jq --raw-output ".aws_region" $CONFIG_PATH)
export AWS_ACCESS_KEY=$(jq --raw-output ".aws_access_key" $CONFIG_PATH)
export AWS_SECRET_KEY=$(jq --raw-output ".aws_secret_key" $CONFIG_PATH)
export ENTITY_ID=$(jq --raw-output ".entity_id" $CONFIG_PATH)
export MQTT_TOPIC=$(jq --raw-output ".mqtt_topic" $CONFIG_PATH)
export MQTT_HOST=$(bashio::services mqtt "host")
export MQTT_USER=$(bashio::services mqtt "username")
export MQTT_PASSWORD=$(bashio::services mqtt "password")

exec /app/venv/bin/python3 /app/main.py
