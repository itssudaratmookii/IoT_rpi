# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

"""
Unit test the comm_mqtt file
"""

__author__ = "Sudarat Tokampang"
import os
import sys
import unittest
from unittest import mock
import paho.mqtt.client as mqtt


sys.path.append(os.path.join("..", "..", "src", "app"))
import src.app.comm_mqtt as comm_mqtt

# installed libraries

class TestComm(unittest.TestCase):
    def test_wrong_sensor(self):
        comm = comm_mqtt.MQTTConn(mock.Mock())
        msg = mqtt.MQTTMessage()
        msg.topic = b"Naresuan/Foobar/data"
        return_code = comm.on_message(None, None, msg)
        print(f"return code: {return_code}")
        self.assertEqual(return_code, 205)

    def test_on_message_data(self):
        msg = mqtt.MQTTMessage()
        print(msg)
        msg.topic = b"Naresuan/Sudarat"
        msg.payload = b'{"datatime": "2023-02-08 10:48:32", "device": "device 2", "temperature": 30}'
        comm = comm_mqtt .MQTTConn(mock.Mock())
        return_code = comm.on_message(None, None, msg)
        print(f"return code: {return_code }")
        self.assertEqual(return_code, 201)

    def test_on_message_status_msg(self):
        comm = comm_mqtt.MQTTConn(mock.Mock())
        msg = mqtt.MQTTMessage()
        msg.topic = b"Naresuan/Sudarat/status"
        msg.payload = b'On'
        return_code = comm.on_message(None, None, msg)
        print(f"return code: {return_code}")
        self.assertEqual(return_code, 0)
        # check that
        print(comm.root.change_status.call_args.args)
        print(comm.root.change_status)
        print(comm.root)
        self .assertEqual(comm.root.change_status.call_args.args,
                          ("Sudarat", True))
        comm.root.change_status.assert_called_with("Sudarat", True)

    def test_data_rx(self):
        comm = comm_mqtt.MQTTConn(mock.Mock())
        msg = mqtt.MQTTMessage()
        msg.topic = b"Naresuan/Sudarat/data"
        msg.payload = b'{"datetime": "2023-02-08 10:48:32", "device": "device 2", "temperature": 30}'
        return_code = comm.on_message(None, None, msg)
        print(f"return code: {return_code}")
        self.assertEqual(return_code, 0)
        print(f"add_data: {comm.root.data.add_data}")
        print(comm.root.data.add_data.call_args)

    def test_wrong_keys(self):
        comm = comm_mqtt.MQTTConn(mock.Mock())
        msg = mqtt.MQTTMessage()
        msg.topic = b"Naresuan/Sudarat/data"
        msg.payload = b'{"dat555time": "2023-02-08 10:48:32", "device": "device 2", "temperature": 30}'
        return_code = comm.on_message(None, None, msg)
        print(f"return code: {return_code}")
        self.assertEqual(return_code, 310)


if __name__ == '__main__':
    unittest.main()
