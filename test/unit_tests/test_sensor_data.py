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

if __name__ == '__main__':
    unittest.main()



if __name__ == '__main__' :
    unittest.main