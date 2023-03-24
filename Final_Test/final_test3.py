# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

"""
Make a class to hold and process incoming
"""

__author__ = "Sudarat Tokampang"

import unittest
from unittest.mock import Mock


class Receive:
    def __init__(self):
        self.data = Data()

    def get_data(self, _data):
        print("get data")
        self.data.add_data(_data)
        return 0


class Data:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)
        return 0


class TestReceive(unittest.TestCase):
    def test_receive_get_data(self):
        """ Unit Test that the get_data method in the class Receive
            will properly call """
        print('test_receive_get_data')
        receive = Receive()
        mock = Mock()
        test_data = " test_receive_get_data "
        receive.get_data = mock
        receive.get_data(test_data)
        receive.get_data.assert_called_with(test_data)


class TestData(unittest.TestCase):
    def test_data(self):
        """ Unit Test that the add_data method appends the
            data to the .data attribute """
        print('test_data')
        data = Data()
        data_testing_add = 'test data'
        data.add_data(data_testing_add)
        print(f"data in Data class: {(data.data)}")
        self.assertListEqual(data.data, [data_testing_add])


class TestReceiveToData(unittest.TestCase):
    def test_rx_to_data(self):
        """ Integration test that sending data using the
            get_data method in the Receive class will
            correctly append it to the data attribute of
            the Data class """
        print(' test_rx_to_data ')
        receive = Receive()
        data_testing = 'test_rx_to_data'
        receive.get_data(data_testing)
        print(f"data: {(receive.data.data)}")
        self.assertListEqual(receive.data.data, [data_testing])