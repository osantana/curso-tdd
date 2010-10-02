import unittest

from roman import to_roman

class TestRoman(unittest.TestCase):
    def test_zero(self):
        self.assertEquals("", to_roman(0))

    def test_one(self):
        self.assertEquals("I", to_roman(1))

