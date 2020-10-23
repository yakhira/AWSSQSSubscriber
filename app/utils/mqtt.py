import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

client = False

def mqtt_publish(host, topic, message):
    if not client:
        client = mqtt.Client("ha-client")
        client.connect(host)
    else:
        client.publish(topic, message)
    
    return client