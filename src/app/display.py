# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

"""
Display
"""

__author__ = "Sudarat Tokampang"


from dataclasses import dataclass
from datetime import datetime, timedelta
import random
import tkinter as tk



from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]


class Display(tk.Frame):
    """
    Display for sensor data implimentsd in a matplotlib.pyplot and
    wrapped in a tkinter Frame

    Attributes
        figure (matplotlib.Figure): figure of the display data
        axis(matplotlib.axes): axis the data
        lines (list[matplotlib.lines]):
        canvas (FigureCanvasTkgg)
    """
    def __init__(self, _parent: tk.Tk):
        tk.Frame.__init__(self, master=_parent)
        self.figure = plt.Figure(figsize=(6, 4))
        self.axis = self.figure.add_subplot()
        self.axis.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        self.lines = self.axis.plot([], [])
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        print(self.lines[0].get_xydata())
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def update_line(self, x_data, y_data):
        """
        Update the data to be display and re-drow the canvas

        Args:
            x_data (list[floats]): x-axis coridinates of the data
            y_data (list[floats]): y-axis coridinates of the data

        Returns:

        """
        self.lines[0].set_xdata(x_data)
        self.lines[0].set_ydata(y_data)
        print(self.lines[0].get_xydata())
        now = x_data[-1]
        self.axis.set_xlim([now - timedelta(minutes=5),
                            now+timedelta(minutes=5)])
        self.axis.set_ylim([0, 40])
        self.canvas.draw()


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
        self .display = Display(_parent)
        self.display.pack()

    def add_data(self):
        self.time .append(datetime.now())
        self.temperature.append(random.randrange(20, 35))
        print(self.time)
        print(self.temperature)
        self.display.update_line(self.time, self.temperature)


if __name__ == '__main__':
    parent = tk.Tk()  #main_gui
    sensor_data = SensorData(parent)
    tk.Button(parent, text="Update data",
              command=sensor_data. add_data).pack()
    parent. mainloop()
