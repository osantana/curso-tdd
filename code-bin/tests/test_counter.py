import unittest

from codebin import get_count, reset_counter

class CounterTest(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def test_counter(self):
        self.assertEquals(0, get_count())
        self.assertEquals(1, get_count())
        self.assertEquals(2, get_count())

    def test_reset_counter(self):
        self.assertEquals(0, get_count())
        reset_counter()
        self.assertEquals(0, get_count())
        reset_counter()
        self.assertEquals(0, get_count())
