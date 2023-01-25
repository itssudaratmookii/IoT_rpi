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

    def __init__(self, _parent):
        self .display = display.Display(_parent)
        self.display.pack()

    def add_data(self, time: datetime, temp: float):
        """
        Append new received data from a sensor and add it to the existing data.


        """
        self.time.append(time)
        self.temperature.append(temp)
        self.display.update_line(self.time, self.temperature)




if __name__ == '__main__':
    _parent = tk.Tk()  #main_gui
    sensor_data = SensorData(_parent)


    tk.Button(_parent, text="Update data",
              command=lambda: sensor_data.add_data(
                  datetime.now(), random.randrange(20, 35))
              ).pack()
    _parent.mainloop()