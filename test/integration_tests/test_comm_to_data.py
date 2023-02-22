# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

"""
Inrtegrating tests that input to the communications class
get passed to the data class correctly
"""

__author__ = "Sudarat Tokampang"

# standard libraries
import unittest
from datetime import datetime
import os
import sys
import unittest
from unittest import mock
import paho.mqtt.client as mqtt

sys.path.append(os.path.join("..", "..", "src", "app"))
# local files
from src.app import comm_mqtt
from src.app import sensor_data


class TestCommToData(unittest.TestCase):
    def test_comm_msg_to_data(self):
        mock_root = mock.Mock()
        mock_root.data = sensor_data.SensorData(None)
        print(f"mock data: {mock_root.data}")
        print(f"mock add_data: {mock_root.data.add_data}")
        comm = comm_mqtt.MQTTConn(mock_root)
        msg = mqtt.MQTTMessage()
        msg.topic = b"Naresuan/Sudarat/data"
        msg.payload = b'{"datetime": "2023-02-08 10:48:32", "device": "device 2", "temperature": 30}'
        return_code = comm.on_message(None, None, msg)
        now = datetime(2023, 2, 8, 10, 48, 32)
        print(f"return code: {return_code}")
        print(f"add_data: {comm.root.data.add_data}")
        print(f"add_time: {mock_root.data.time}")
        print(f"add_temperature: {mock_root.data.temperature}")
        self.assertEqual([now], mock_root.data.time)
        self.assertEqual([30], mock_root.data.temperature)


if __name__ == '__main__':
    unittest.main()