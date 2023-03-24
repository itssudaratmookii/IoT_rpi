# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

"""
Inrtegrating tests that input to the communications class
get passed to the data class correctly
"""

__author__ = "Sudarat Tokampang"

# standard libraries
from datetime import datetime as dt
import json
import time

import paho.mqtt.client as mqtt

from src .app .config import*

client = mqtt.Client()
client.connect(HIVEMQTT_BROKER, HIVEMQTT_PORT)
client.loop_start()

temperature = 0

while True :
    payload ={'datetime': dt.now().strftime("%Y-%m-%d %H:%M:%S"),
              "device": "device Sudarat",
              "temperature": temperature}
    temperature = (temperature+1) % 10
    print(f'payload: {payload }')

    client.publish(PUBLIST_DATA_TOPIC, json.dumps((payload)))

    time.sleep(5)
