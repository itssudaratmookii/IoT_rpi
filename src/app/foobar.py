# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

""" Document string (Doc String)
A graphical user interfacr to observe sensor data
from a remotr sensor through a matt communication channel
"""

__author__ = "Sudarat Tokampang"
import tkinter as tk

import json
from datetime import datetime

print(datetime .now().strftime('%Y-%m-%d %H:%M:%S'))

data = {'datatime': '2023-02-08 10:48:32', 'device': 'device 2',
        'temperature': 30}
#{} - curly brackets [] - square brackets

print(data)
print(type(data))
print(data.keys())
for key in data.keys():
    print(f"key: {key}, value: {data[key]}")

mqtt_data = json.dumps(data)
print(f"mqtt data: {mqtt_data}")

