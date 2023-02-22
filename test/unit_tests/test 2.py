# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

"""
Test the methods of the sensor_data.SensorData class
"""

__author__ = "Sudarat Tokampang"

# standard libraries
from datetime import datetime, timedelta
import os
import sys
import unittest

sys.path.append(os.path.join("..", "..", "src", "app"))
# local files
from src.app import sensor_data


class TestSensorData(unittest.TestCase):
    def test_add_data(self):
        sensor_class = sensor_data.SensorData(None)
        print(sensor_class)

        now = datetime(2023, 1, 24, 10, 50, 12)
        sensor_class.add_data(now, 5)
        self.assertEqual([now], sensor_class .time)
        self.assertEqual([5], sensor_class.temperature)
        #add
        now2 = datetime(2023, 1, 24, 10, 50, 12)
        sensor_class.add_data(now2, 10)
        print(f"time: {sensor_class.time}")
        print(f"temp: {sensor_class.temperature}")
        self.assertEqual([now, now2], sensor_class.time)
        self.assertEqual([5, 10], sensor_class.temperature)

    def test_display_update_line_called(self):
        """ Test that the update_line method is called correctly.
         Use the test_sensor_ui code for an example """
        # mock the display.Display class in the sensor_data module
        sensor_class = self.sensor_class
        # print('======')
        # print(sensor_class.add_data)
        # print(f"temp: {sensor_class.temperature}")
        # add 1 data point and check it is added correctly
        now = datetime(2023, 1, 24, 10, 50, 12)
        sensor_class.add_data(now, 5)
        # check that the self.display.update_line is called with the
        # correct arguments
        # print(f"update_line: {sensor_class.display.update_line}")
        # print(f"args: {self.mock_display.update_line}")
        # print(f"args2: {sensor_class.display.update_line.call_args}")
        # print(self.mock_display)
        sensor_class.display.update_line.assert_called_with([now], [5])

if __name__ == '__main__':
    unittest.main