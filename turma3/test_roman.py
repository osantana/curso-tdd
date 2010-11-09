import unittest

def roman(d):
    if d == 0:
        raise ValueError("There is no 0 in roman algarisms")

    exceptions = (
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    )

    res = ""
    while d:
        for exc, r in exceptions:
            if d >= exc:
                res = res + r
                d = d - exc
                break
    return res

    if d > 40:
        return roman(40) + roman(d - 40)
    elif d > 10 and d < 40:
        return roman(10) + roman(d - 10)
    elif d > 5 and d < 9:
        return roman(5) + roman(d - 5)

    return dic.get(d, "I" * d)

class TestRoman(unittest.TestCase):
    def test_zero_raises_value_error(self):
        self.assertRaises(ValueError, roman, 0)

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

    def test_eight(self):
        self.assertEquals("VIII", roman(8))

    def test_nine(self):
        self.assertEquals("IX", roman(9))

    def test_ten(self):
        self.assertEquals("X", roman(10))

    def test_eleven(self):
        self.assertEquals("XI", roman(11))

    def test_twelve(self):
        self.assertEquals("XII", roman(12))

    def test_fourteen(self):
        self.assertEquals("XIV", roman(14))

    def test_fifteen(self):
        self.assertEquals("XV", roman(15))

    def test_sixteen(self):
        self.assertEquals("XVI", roman(16))

    def test_nineteen(self):
        self.assertEquals("XIX", roman(19))

    def test_twenty(self):
        self.assertEquals("XX", roman(20))

    def test_fourty(self):
        self.assertEquals("XL", roman(40))

    def test_fourty_one(self):
        self.assertEquals("XLI", roman(41))

    def test_fourty_two(self):
        self.assertEquals("XLII", roman(42))

