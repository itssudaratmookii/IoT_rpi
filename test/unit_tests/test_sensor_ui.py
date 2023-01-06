# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

""" Document string (Doc String)
A graphical user interfacr to observe sensor data
from a remotr sensor through a matt communication channel
"""

__author__ = "Sudarat Tokampang"

#  standard libraries
import os
import sys
import unittest
from unittest import mock

sys.path.append(os.path.join("..", "..", "src", "app"))
# local files
from src.app import main_gui



class TestSensorUI(unittest.TestCase) :
    def test_button_click_change_running(self):
        gui = main_gui.SensorUI()
        print(gui.running)
        self.assertFalse(gui.running)
        gui.button_click()
        print(gui.running)
        self.assertTrue(gui.running)

    def test_button_click_call_comm(self):

        with mock.patch("main_gui.comm_mqtt.MQTTConn") as mocked_comm:
            gui = main_gui.SensorUI()
            gui.button_click()
            gui.comm.publish.assert_called()
            gui.comm.publish: mock.MagicMock
            gui.comm.publish.assert_called_with("On")



if __name__ == '__main__':
    unittest.main()