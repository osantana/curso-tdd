import unittest

from roman import to_roman

class TestRoman(unittest.TestCase):
    def test_zero(self):
        self.assertEquals("", to_roman(0))
