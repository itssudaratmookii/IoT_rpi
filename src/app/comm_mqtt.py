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


class MQTTConn:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connection
        #self.client.on_subscribe = self.on_subscription
        self.client.on_message = self.on_message
        self.client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
        self.client.loop_start()

    def publish(self, topic, message):
        self.client.publish(topic, message)

    def on_connection(self, *args):
        """call back for when mqtt connects to the broken
        and prints out acknowledgment and subscribes"""
        print("Connected")
        self.client.subscribe(SUBSCRIBE_TOPIC)

    @staticmethod
    def on_message(client, user_data, msg: mqtt.MQTTMessage):
        print("got message: ", msg.payload)


if __name__ == '__main__':
    client = MQTTConn()
    while True:
        client.publish(PUBLIST_TOPIC,
                        "hello_this is MOOK")
        time.sleep(10)


