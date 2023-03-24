""" Document string (Doc String)
A graphical user interface to observe sensor data
from a remote sensor through a matt communication channel
"""

__author__ = "Sudarat Tokampang"

# standard libra
import tkinter as tk
import final_comm_mqtt   # MQTT

NAMES = ["Pick Rock", "Pick Scissor", "Pick Paper"]


class SensorUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.comm = final_comm_mqtt.MQTTConn(self)  # MQTT
        self.comm.on_message()
        self.running = False
        self.button1 = tk.Button(self, text="Hello World",
                                command=self.button1_click)
        self.button1.pack(side=tk.TOP)

        # self.button2 = tk.Button(self, text="Pick Scissors ",
        #                         command=self.button2_click)
        # self.button2.pack(side=tk.TOP)
        #
        # self.button3 = tk.Button(self, text="Pick Paper ",
        #                         command=self.button3_click)
        # self.button3.pack(side=tk.TOP)
        #
        # self.label = tk.Label(text="You Pick")
        # self.label.pack(side=tk.TOP)
        #
        # self.label1 = tk.Label(text="Computer choose")
        # self.label1.pack(side=tk.TOP)
        #
        # self.label2 = tk.Label(text="You")
        # self.label2.pack(side=tk.TOP)


    def button1_click(self):
        """
        Toggle the stat of the sensor True -> False or False -> True,
        update the text of the run button, update the local StatusButton,
        and send the proper mqtt message
        """
        # self.label.config(text="You Click")

        msg = "Hello World"  # MQTT
        self.comm.publish(msg)    # MQTT



    # def button2_click(self):
    #     self.label.config(text="You pick Scissor")
    #     msg = "Scissors"  # MQTT
    #     self.comm.publish(msg)  # MQTT
    #
    #
    #
    # def button3_click(self):
    #     self.label.config(text="You pick Paper")
    #     msg = "Paper"  # MQTT
    #     self.comm.publish(msg)  # MQTT

if __name__ == "__main__":
    app = SensorUI()   # application a class ot tkinter.Tk
    # geometry is a method of the tkinter.Tk class that
    # sets the size of the app window. It takes a
    # string as on argument
    app.geometry("400x400")
    app.title('FINAL')
    app.mainloop()  # mainloop is method of tkinter.Tk
    # methods are function of classes