# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

"""
Test that when data is input to the sensor_data.Sensor data
it is passed and handled correctly by the display.Display
"""

__author__ = "Sudarat Tokampang"


# standard libraries
import unittest
from datetime import datetime
import os
import sys
import unittest
from unittest import mock

sys.path.append(os.path.join("..", "..", "src", "app"))
# local files
from src.app import display
from src.app import sensor_data


class TestDataToDisplay(unittest.TestCase):
    def test_data_to_display(self):
        """
        Test that adding data to the data class makes the
        pyplot graph have the correct xy data

        """
        sensor_class = sensor_data.SensorData(None)

        # add 1 data point and check it added correctly
        now = datetime(2023, 1, 24, 10, 50, 12)
        sensor_class.add_data(now, 5)
        # print(f"sensor.display; {type(sensor_class.display) }"
        #start_time = datetime(1970, 1, 1,)
        # print(f"start time: {start_time}")
        # print(f"diff: {start_time-now}")
        # print(f"plt data:{sensor_class.display.lines[0].get_xydata()}")
        xy_data = sensor_class.display.lines[0].get_xydata().tolist()
        # print(f"plt data: {xy_data}")
        # print(f"xy data type: {type(xy_data)}")
        self.assertListEqual([[19381.45152777778, 5.0]], xy_data)

    def test_draw_is_called(self):
        sensor_class = sensor_data.SensorData(None)
        sensor_class.display.canvas.draw = mock.Mock()
        # add 1 data point and check it added correctly
        now = datetime(2023, 1, 24, 10, 50, 12)
        sensor_class.add_data(now, 5)
        sensor_class.display.canvas.draw.assert_called()


if __name__ == '__main__':
    unittest.main()a