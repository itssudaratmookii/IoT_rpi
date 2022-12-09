# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

""" Document string (Doc String)
A graphical user interface to observe sensor data
from a remote sensor through a matt communication channel
"""

__author__ = "Sudarat Tokampang"

# standard libra
import tkinter as tk


class StatusButton:
    """ Display the status using a canvas

    Attributes:
        circle: object used to display the status
        canvas (tk.Canvas): canvas the circle is in
        color (str): color the circle will show

    """

    def __init__(self, parent):
        # make a variable to change color
        self.color = 'red'  # =assignment
        self.canvas = tk.Canvas(parent, width=120, height=120)
        self.circle = self.canvas.create_oval(10, 10, 110, 110,
                                              fill=self.color)

        self.canvas.pack()

    def toggle_color(self):
        """ Toggle the color between red and green """
        if self.color == 'red':
            self.color = 'green'
        elif self.color == 'green':
            self.color = 'red'
        self.canvas.itemconfig(self.circle, fill=self.color)


app = tk .Tk()  # application a class ot tkinter.Tk
# geometry is a method of the tkinter.Tk class that
# sets the size of the app window. It takes a
# string as on argument
app.geometry("400x400")
status_btn = StatusButton(app)
print(status_btn)
status_btn2 = StatusButton(app)
print(status_btn2)

# make a button (tkinter class) and put it in the app
# button takes 3 argument, app-where to put the button
# text - key word argument
tk.Button(app, text="Toggle Circle 1",
          command=status_btn.toggle_color).pack()
tk.Button(app, text="Toggle Circle 2",
          command=status_btn2.toggle_color).pack()

app.mainloop()  # mainloop is method of tkinter.Tk
# methods are function of classes
