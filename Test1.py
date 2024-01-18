import logging
import sys
import unittest

from xmlrunner.extra.xunit_plugin import transform


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_add(self):
        self.assertEqual(2 + 2, 4)


if __name__ == '__main__':
    unittest.main()

