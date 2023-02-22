# Copyright (c) 2023 Kyle Lopin <kylel@nu.ac.th>

"""
"""

__author__ = "Sudarat tokampang"

# standard libraries
from datetime import datetime
import os
import sys
import unittest

sys.path.append(os.path.join("..", "..", "src", "app"))
# local files
from src.app import display


class TestDisplay(unittest.TestCase):
    def test_update_line(self):
        """ Test that calling the update_line method
        in display.Display works correctly """
        _display = display.Display(None)
        time = [datetime(2023, 1, 24, 10, 50, 12)]
        temps = [5]
        _display.update_line(time, temps)
        print("getting x y data")
        print(_display.lines[0].get_xydata())
        # assignment: use asserts to check update_line works correctly


if __name__ == '__main__':
    unittest.main()