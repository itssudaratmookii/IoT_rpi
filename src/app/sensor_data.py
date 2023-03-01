# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

"""
Make a class to hold and process incoming
"""

__author__ = "Sudarat Tokampang"

from dataclasses import dataclass
from datetime import datetime, timedelta
import random
import tkinter as tk


import display

class SensorHubData:
    """
    Parent class to hold different sensor data series
    sensor data series are held in the attribute dictionary . sensors
    with the keys of "{device}{data_type}" and values of SensorData, ie:
    "{device 2 temperature": SensorData}

    Attributes:
         sensor (dict): hold a series of SensorData classs
         display (Display): chila that will display the data of the class

    """
    sensors = {}

    def __init__(self, _parent: tk.Tk):
        self.display = display.Display(_parent)
        self.display.pack()

    def add_data(self, sensor, time, temp):
        print(f"add data: {sensor}, {time}, {time}")
        sensor_key = f"{sensor} temp"
        print(sensor_key)
        if sensor_key not in self.sensors:
            print(f"add {sensor_key} to sensors")
            self.sensors[sensor_key] = SensorData()
        _sensor_data = self.sensors[sensor_key]
        _sensor_data.add_data(time, temp)
        # self.sensors[sensor_key].add_data(time, temp)

        self.display.update_line(_sensor_data.time,
                                 _sensor_data.temperature,
                                 sensor)


@dataclass
class SensorData:
    """
    Data class to hold 1 sensor time series data

    Attributes
        time (list[datetime]): time stamps of when ten sensor read data
        temperature (list[floots]): sensor data
        display (Display): chid that will display the data of this class
    """
    time = []
    temperature = []

    def add_data(self, time: datetime, temp: float):
        """
        Append new received data from a sensor and add it to the existing data.
        """
        print("ll")
        self.time.append(time)
        self.temperature.append(temp)
        print(self.time)



if __name__ == '__main__':
    _parent = tk.Tk()  #main_gui
    sensor_data = SensorData(_parent)


    tk.Button(_parent, text="Update data",
              command=lambda: sensor_data.add_data(
                  datetime.now(), random.randrange(20, 35))
              ).pack()
    _parent.mainloop()