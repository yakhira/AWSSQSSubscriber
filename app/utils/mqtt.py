import logging
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

client = False

mqtt.enable_logger(logging.getLogger(__name__))

def mqtt_publish(host, topic, message):
    global client

    if not client:
        client = mqtt.Client("ha-client")
        client.connect(host)

    client.publish(topic, message)
    
    
    return client