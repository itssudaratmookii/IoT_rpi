# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

"""
communicate with the HIVEMQ broker to receive
sensor data,using the paho matt library
"""

__author__ = "Sudarat Tokampang"

import paho.mqtt.client as mqtt
from datetime import datetime
import json
import time

# installed library
import paho.mqtt.client as mqtt
from config import *


class MQTTConn:
    """
    Use the paho library to connect to the HIVE MQ mqtt broker

    Attributes
        root(main_gui.SensorUI): root user interface app
        root.data(sensor_data.SensorHubData): master and class for all sensor
        client (mqtt.Client): paho client for mqtt communication
    """
    def __init__(self, root: 'main_gui.SensorUI'):
        self.root = root
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connection
        #self.client.on_subscribe = self.on_subscription
        self.client.on_message = self.on_message
        self.client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
        self.client.loop_start()

    def publish(self, message, is_data = True):
        """
        Send a message to the HIVE MQ broker using the PUBLISH_TOPIC
        Args:
            message(str): massage to send

        Returns:

        """
        publish_topic = PUBLIST_STATUS_TOPIC
        if is_data:
            publish_topic = PUBLIST_DATA_TOPIC
        self.client.publish(publish_topic, message)

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
        if len(msg.topic.split('/')) != 3:
            return 201
        sensor = msg .topic .split('/')[1]
        type = msg.topic .split('/')[2]
        print("message from: ", sensor)
        if sensor not in SENSOR_LIST:
            print("Unrecognized sensor, returing")
            return 205  # error code
        if type == "status":
            print("parsing status")
            return self.parse_status_msg(sensor, msg.payload)
        elif type == 'data':
            print("parse data")
            return self.parse_data_msg(msg.payload)
        return 0  # no errors

    def parse_data_msg(self, msg):
        print(f"parse msg:{msg}")
        json_data = json.loads(msg)
        print(f"json data: {json_data}")
        print(f"json_data type: {type(json_data)}")
        if "datetime" not in json_data.keys():
            return 310
        if "device" not in json_data.keys():
            return 310
        if "temperature" not in json_data.keys():
            return 310
        # convert datetime from a string to a date time
        date_time = datetime.strptime(json_data["datetime"],
                                      "%Y-%m-%d %H:%M:%S")

        print(f"converted date_time: {date_time}")
        self.root.data.add_data(json_data["device"],
                                date_time,
                                json_data["temperature"])
        return 0

    def parse_status_msg(self, sensor, msg):
        print(f"gor msg:{msg } from:{sensor}")
        if msg == b"On":
            sensor_state = True
        elif msg == b"Off":
            sensor_state = False
        else:
            return
        self.root.change_status(sensor, sensor_state)
        return 0


if __name__ == '__main__':
    test_client = MQTTConn(None)
    while True:
        test_client.publish("{'datetime': '2023-02-08 10:48:32', 'device': 'device 2', 'temperature': 30}")
        # test_client.publish("Off")
        time.sleep(10)


