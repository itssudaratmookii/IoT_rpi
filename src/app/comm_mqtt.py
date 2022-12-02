# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

"""
communicate with the HIVEMQ broker to receive
sensor data,using the paho matt library
"""

__author__ = "Sudarat Tokampang"


import time

# installed library
import paho.mqtt.client as mqtt

HIVEMQTT_PORT = 1883 # CONSTANT
HIVEMQTT_BROKER = "broker.hivemq.com"
PUBLIST_TOPIC = "Naresuan/Sudarat"
SUBSCRIBE_TOPIC = "Naresuan/+"

def on_subscription(*args):
    print("subscribed: ", args)

def on_connection(*args):
    """call back for when mqtt connects to the broken
    and prints out acknowledgment and subscribes"""
    print("Connected")
    client.subscribe(SUBSCRIBE_TOPIC)



def on_message(client, user_data, msg: mqtt.MQTTMessage):
    print("got message: ", msg.payload)



client = mqtt.Client()
client.on_connect = on_connection
client .on_subscribe = on_subscription
client.on_message = on_message
client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
client.loop_start()
while True:
    client.publish(PUBLIST_TOPIC,
                   "hello_this is MOOK")
    time.sleep(10)

app.mainloop()
