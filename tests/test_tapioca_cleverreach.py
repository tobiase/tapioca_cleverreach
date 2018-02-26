# coding: utf-8

import unittest

from tapioca_cleverreach import Cleverreach


class TestTapiocaCleverreach(unittest.TestCase):

    def setUp(self):
        self.wrapper = Cleverreach()


if __name__ == '__main__':
    unittest.main()
