# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

"""
communicate with the HIVEMQ broker to receive
sensor data,using the paho matt library
"""

__author__ = "Sudarat Tokampang"

import paho.mqtt.client as mqtt
import main_gui

import time

# installed library
import paho.mqtt.client as mqtt

HIVEMQTT_PORT = 1883  # CONSTANT
HIVEMQTT_BROKER = "broker.hivemq.com"
PUBLIST_TOPIC = "Naresuan/Sudarat"
SUBSCRIBE_TOPIC = "Naresuan/+"


class MQTTConn:
    """
    Use the paho library to connect to the HIVE MQ mqtt broker

    Attributes
        root(main_gui.SensorUI): root user interface app
        client (mqtt.Client): paho client for mqtt communication
    """
    def __init__(self, root: main_gui.SensorUI):
        self.root = root
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connection
        #self.client.on_subscribe = self.on_subscription
        self.client.on_message = self.on_message
        self.client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
        self.client.loop_start()

    def publish(self, message):
        """
        Send a message to the HIVE MQ broker using the PUBLISH_TOPIC
        Args:
            message(str): massage to send

        Returns:

        """
        self.client.publish(PUBLIST_TOPIC, message)

    def on_connection(self, *args):
        """call back for when mqtt connects to the broken
        and prints out acknowledgment and subscribes"""
        print("Connected")
        self.client.subscribe(SUBSCRIBE_TOPIC)


    def on_message(self, client, user_data, msg: mqtt.MQTTMessage):
        """
        Callback when receiving message
        Args:
            client:
            user_data:
            msg(mqtt.MQTTMessage): message received

        """
        print("got message: ", msg.payload)
        print("from topic", msg.topic)
        name = msg .topic .split('/')[-1]
        print("message from: ", name)
        if msg.payload == b"On":
            sensor_state = True
        else:
            sensor_state = False
        self.root.change_status(name,
                                sensor_state)


if __name__ == '__main__':
    test_client = MQTTConn(None)
    while True:
        test_client.publish("hello_this is MOOK")
        time.sleep(10)


