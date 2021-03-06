import unittest

from roman import to_roman

class TestRoman(unittest.TestCase):
    def test_zero(self):
        self.assertEquals("", to_roman(0))

    def test_one(self):
        self.assertEquals("I", to_roman(1))

    def test_two(self):
        self.assertEquals("II", to_roman(2))

    def test_three(self):
        self.assertEquals("III", to_roman(3))

    def test_four(self):
        self.assertEquals("IV", to_roman(4))

    def test_five(self):
        self.assertEquals("V", to_roman(5))

    def test_six(self):
        self.assertEquals("VI", to_roman(6))

    def test_nine(self):
        self.assertEquals("IX", to_roman(9))

    def test_ten(self):
        self.assertEquals("X", to_roman(10))

    def test_fourteen(self):
        self.assertEquals("XIV", to_roman(14))

    def test_fourty(self):
        self.assertEquals("XL", to_roman(40))

    def test_fourty_four(self):
        self.assertEquals("XLIV", to_roman(44))

    def test_fifty(self):
        self.assertEquals("L", to_roman(50))

    def test_ninety(self):
        self.assertEquals("XC", to_roman(90))

    def test_hundred(self):
        self.assertEquals("C", to_roman(100))

    def test_four_hundred(self):
        self.assertEquals("CD", to_roman(400))

    def test_five_hundred(self):
        self.assertEquals("D", to_roman(500))

    def test_nine_hundred(self):
        self.assertEquals("CM", to_roman(900))

    def test_one_thousand(self):
        self.assertEquals("M", to_roman(1000))

    def test_other_numbers(self):
        self.assertEquals("XXVII", to_roman(27))
        self.assertEquals("LXXXIX", to_roman(89))
        self.assertEquals("CXLV", to_roman(145))
        self.assertEquals("DCXCI", to_roman(691))
        self.assertEquals("MCMLXXXIII", to_roman(1983))
        self.assertEquals("MMCDXII", to_roman(2412))
        self.assertEquals("MMMCCCIX", to_roman(3309))

