#Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

""" Document string (Doc String)
A graphical user interfacr to observe sensor data
from a remotr sensor through a matt communication channel
"""

__author__ = "Sudarat Tokampang"


import tkinter

# make a variable to change color
color ='red' # =assignment

# made a python function to print "Hello World"
# def - define
def hello_world():
    global color
    print("Hello World")
    if color == 'red':
       color ='green'
    elif color =='green':
         color ='yellow'
    elif color == 'yellow':
         color = 'red'

    canvas.itemconfig(circle, fill=color)



app = tkinter .Tk() #application a class ot tkinter.Tk
# geometry is a method of the tkinter.Tk class that
# sets the size of the app window. It takes a
# string as on orgument
app.geometry ("400x400")
canvas = tkinter.Canvas(app, width=120, height=120)
circle = canvas.create_oval(10, 10, 110, 110,
                            fill= "green")
canvas.pack()

# make a botton (tkiner class) and put it in the app
# botton takes 3 argument, app-where to put the button
# text - key word argument
tkinter.Button(app, text="Hello World",
               command=hello_world).pack()

app.mainloop() #mainloop is method of tkinter.Tk
# mathods are function of classes