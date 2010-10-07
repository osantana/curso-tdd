import unittest

from roman import roman

class TestRoman(unittest.TestCase):
    def test_zero(self):
        self.assertEquals("", roman(0))

    def test_one(self):
        self.assertEquals("I", roman(1))

    def test_two(self):
        self.assertEquals("II", roman(2))

    def test_three(self):
        self.assertEquals("III", roman(3))

    def test_four(self):
        self.assertEquals("IV", roman(4))

    def test_five(self):
        self.assertEquals("V", roman(5))

    def test_six(self):
        self.assertEquals("VI", roman(6))

    def test_seven(self):
        self.assertEquals("VII", roman(7))

    def test_nine(self):
        self.assertEquals("IX", roman(9))

    def test_ten(self):
        self.assertEquals("X", roman(10))

    def test_fourteen(self):
        self.assertEquals("XIV", roman(14))

    def test_nineteen(self):
        self.assertEquals("XIX", roman(19))

    def test_twenty(self):
        self.assertEquals("XX", roman(20))

    def test_fourty(self):
        self.assertEquals("XL", roman(40))

    def test_fifty(self):
        self.assertEquals("L", roman(50))

    def test_ninety(self):
        self.assertEquals("XC", roman(90))

    def test_one_hundred(self):
        self.assertEquals("C", roman(100))

    def test_two_hundred(self):
        self.assertEquals("CC", roman(200))




