import logging
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

client = False

def mqtt_publish(host, user, password, topic, message):
    global client

    if not client:
        client = mqtt.Client()
        client.username_pw_set(user, password)
        client.enable_logger(logging.getLogger(__name__))
        client.connect(host)

    if client.publish(topic, message):
        logging.info(f'Published topic {topic}.')

    return client