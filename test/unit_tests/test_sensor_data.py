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
from unittest import mock

sys.path.append(os.path.join("..", "..", "src", "app"))
# local files
from src.app import sensor_data


class TestSensorData(unittest.TestCase):
    def setUp(self) -> None:
        """
        """
        with mock.patch("sensor_data.display.Display") as mock_display:
            self.sensor_class = sensor_data.SensorHubData(None)
            print(self.sensor_class.sensors)
            print('====')
            for _key in self.sensor_class.sensors:
                _sensor_data = self.sensor_class.sensors[_key]
                print(_sensor_data)
                _sensor_data.temperature = []
                _sensor_data.time = []
            self.sensor_class.temperature = []
            self.sensor_class.time = []
            self.mock_display = mock_display

    def test_add_data(self):
        sensor_class = self.sensor_class
        print(sensor_class)
        now = datetime(2023, 1, 24, 10, 50, 12)
        print(f"start: {sensor_class.sensors}")
        sensor_class.add_data("device 2", now, 5)
        print(f"middle: {sensor_class.sensors}")
        self.assertTrue("device 2" in sensor_class.sensors)
        sensor = sensor_class.sensors["device 2"]

        self.assertEqual([now], sensor.time)
        self.assertEqual([5], sensor.temperature)
        # add second data point
        now2 = datetime(2023, 1, 24, 10, 50, 12)
        sensor_class.add_data("device 2", now2, 10)
        print(f"time: {sensor.time}")
        print(f"temp: {sensor.temperature}")
        self.assertEqual([now, now2], sensor.time)
        self.assertEqual([5, 10], sensor.temperature)

    # TODO: Move this test to TestSensorHubData
    # def test_display_update_line_called(self):
    #     with mock.patch("sensor_data.SensorData.display") as sensor_class:
    #         sensor_class = sensor_data.SensorData(None)
    #         print('=====')
    #         print("sensor class", sensor_class)
    #         print(f"temp: {sensor_class.temperature}")
    #         print(sensor_class)
    #         now = datetime(2023, 1, 24, 10, 50, 12)
    #         sensor_class.add_data("device 2", now, 5)
    #         print(f"update_line: {sensor_class.display.update_line}")
    #         print(f"args: {sensor_class.display.update_line.call_args.args}")
    #         sensor_class.display.update_line.assert_called_with([now, 5])


class TestSensorHubData(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
