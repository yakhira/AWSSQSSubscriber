import logging
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

client = False

def mqtt_publish(host, user, password, topic, message):
    global client

    if not client:
        client = mqtt.Client("ha-client")
        client.username_pw_set(user, password)
        client.connect(host)
    logging.info(client.publish(topic, message))
    
    return client