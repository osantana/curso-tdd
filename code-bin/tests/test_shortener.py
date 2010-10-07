import unittest

from codebin import short

class ShortnerTest(unittest.TestCase):
    def test_zero_to_A(self):
        self.assertEquals("A", short(0))

    def test_one_to_B(self):
        self.assertEquals("B", short(1))

    def test_twenty_five_to_Z(self):
        self.assertEquals("Z", short(25))

    def test_twenty_six_to_a(self):
        self.assertEquals("a", short(26))

    def test_fifty_one_to_z(self):
        self.assertEquals("z", short(51))

    def test_fifty_two_to_zero(self):
        self.assertEquals("0", short(52))

    def test_sixty_two_to_nine(self):
        self.assertEquals("9", short(61))

    def test_others(self):
        res = ""
        for d in range(62, 82):
            res += short(d)
        self.assertEquals("!$()*-./:;<>[]^_`{|}", res)

    def test_eighty_two_to_BA(self):
        self.assertEquals("BA", short(82))

    def test_big_integer_to_BAA(self):
        self.assertEquals("BAA", short(6724))
