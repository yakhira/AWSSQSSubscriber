import logging
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

client = False

def mqtt_publish(host, topic, message):
    global client

    if not client:
        client = mqtt.Client("ha-client")
        client.enable_logger(logging.getLogger(__name__))
        client.connect(host)

    client.publish(topic, message)
    
    
    return client