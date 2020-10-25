import logging
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

client = False

def mqtt_publish(host, user, password, topic, message):
    # global client

    # if not client:
    #     client = mqtt.Client()
    #     client.username_pw_set(user, password)
    #     client.enable_logger(logging.getLogger(__name__))
    #     client.connect(host)

    # if client.publish(topic, message):
    #     logging.info(f'Published topic {topic}.')

    # return client
    publish.single(
        topic,
        message,
        hostname=host,
        auth={
            'username': user,
            'password': password
        },
        keepalive=120
    )
def on_publish(client, userdata, mid):
    if len(userdata) == 0:
        client.disconnect()
    else:
        _do_publish(client)