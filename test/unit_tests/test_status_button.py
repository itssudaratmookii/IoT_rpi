# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

"""
Run unit tests on this StatusButton class in the main_gui file
"""

__author__ = "Sudarat Tokampang"

#  standard libraries
import os
import sys
import unittest

#print(os.getcwd())
#print(os.path.abspath(os.path .join("..", "..", "src", "app")))
sys.path.append(os.path.join("..", "..", "src", "app"))
# local files
from src.app import main_gui



class TestStatusButton(unittest.TestCase):
    def test_toggle_color(self):
        status_button = main_gui.StatusButton(None, "Sudarat")
        color = (status_button.canvas.itemcget(status_button.circle,
                                              'fill'))
        self.assertEqual(color, "red",
                         msg="Status color not changed correctly")
        self.assertEqual(status_button.color, "red",
                         msg="Status color not changed correctly")

        status_button.toggle_color(True)
        print(status_button.canvas.itemcget(status_button.circle,
                                              'fill'))
        print(status_button.color)
        color = (status_button.canvas.itemcget(status_button.circle,
                                               'fill'))
        self.assertEqual(color, "green",
                         msg="Status color not changed correctly")
        self.assertEqual(status_button.color, "green",
                         msg="Status color not changed correctly")

        status_button.toggle_color(True)
        print(status_button.canvas.itemcget(status_button.circle,
                                            'fill'))
        print(status_button.color)
        color = (status_button.canvas.itemcget(status_button.circle,
                                               'fill'))
        self.assertEqual(color, "green",
                         msg="Status color not changed correctly")
        self.assertEqual(status_button.color, "green",
                         msg="Status color not changed correctly")

        status_button.toggle_color(False)
        print(status_button.canvas.itemcget(status_button.circle,
                                            'fill'))
        print(status_button.color)
        color = (status_button.canvas.itemcget(status_button.circle,
                                               'fill'))
        self.assertEqual(color, "red",
                         msg="Status color not changed correctly")
        self.assertEqual(status_button.color, "red",
                         msg="Status color not changed correctly")


if __name__ =='__main__':
    unittest.main()
