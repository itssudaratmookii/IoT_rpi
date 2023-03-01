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
    canvas = None
    lines = {}

    def __init__(self, _parent: tk.Tk):
        tk.Frame.__init__(self, master=_parent)
        self.figure = plt.Figure(figsize=(6, 4))
        self.axis = self.figure.add_subplot()
        self.axis.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def update_line(self, x_data, y_data: list,
                    label: str):
        """
        Update the data to be display and re-drow the canvas

        Args:
            x_data (list[floats]): x-axis coridinates of the data
            y_data (list[floats]): y-axis coridinates of the data

        Returns:

        """
        if label not in self.lines:
            print(f"add label: {label}")
            self.lines[label], = self.axis.plot(x_data, y_data,
                                                label=label)
            self.axis.legend()
            self.canvas.draw()
            return

        self.lines[label].set_xdata(x_data)
        self.lines[label].set_ydata(y_data)
        now = x_data[-1]
        self.axis.set_xlim([now - timedelta(minutes=5),
                            now+timedelta(minutes=5)])
        self.axis.set_ylim([0, 40])
        self.canvas.draw()



if __name__ == '__main__':
    parent = tk.Tk()  #main_gui
    sensor_data = SensorData(parent)
    tk.Button(parent, text="Update data",
              command=sensor_data. add_data).pack()
    parent. mainloop()
