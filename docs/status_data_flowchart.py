# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

"""
Make a flowchart diagramming how that
status data moves into the program
"""


__author__ = "Sudarat Tokampang"

# installed libraries
import schemdraw
from schemdraw import flow

with schemdraw .Drawing() as d:
    d += flow.Start(w=6).label("Data send from HIVEQM")
    d += flow.Arrow().down(d.unit/2)
    d += flow.Data(w=6).label("receive into on_message\n"
                              "in comm_mqtt.MQTTConn")
    d += flow.Arrow().down(d.unit / 2)
    d += flow.Process (w=6).label("process input message\n "
                                  "into a sensor status state")
    d += flow.Arrow().down(d.unit / 2)
    d += flow.Data(w=7).label("send sensor status to\n"
                              "main_gui.SensorUI.change_status")
    d += flow.Arrow().down(d.unit / 2)
#    d += (d1 := flow.Decision(w=6, h=6, E="No").label(
#        "Is the name from\nthe data found in\nthe NAMES list"))

    d1 = d.add(flow.Decision(w=6, h=6, E="No", S="Yes").label(
        "Is the name from\nthe data found in\nthe NAMES list"))
    d += flow.Arrow().right(d.unit / 2).at(d1.E)
    d += flow.Terminal(w=5, label="Exit with no change").anchor('W')
    d += flow.Arrow().down(d.unit / 2) .at(d1.S)
    d += flow.Process(w=10).label("call main_gui.StatusButton.toggle_color\n"
                                 "and est the propre color the indicator")
