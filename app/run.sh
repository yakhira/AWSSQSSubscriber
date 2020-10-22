#!/usr/bin/env bashio
set +u

CONFIG_PATH=/data/options.json
SYSTEM_USER=/data/system_user.json

export SQS_QUEUE=$(jq --raw-output ".sqs_queue" $CONFIG_PATH)
export AWS_REGION=$(jq --raw-output ".aws_region" $CONFIG_PATH)
export AWS_ACCESS_KEY=$(jq --raw-output ".aws_access_key" $CONFIG_PATH)
export AWS_SECRET_KEY=$(jq --raw-output ".aws_secret_key" $CONFIG_PATH)
export ENTITY_ID=$(jq --raw-output ".entity_id" $CONFIG_PATH)

exec /usr/bin/python3 $APPDIR/main.py