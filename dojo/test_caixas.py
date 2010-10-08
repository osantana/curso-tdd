import unittest

def somapilha(caixas):
    return caixas[0][0]

class DojoTest(unittest.TestCase):

    def test_uma_caixa(self):
        caixas = [(10,15)]
        self.assertEquals(10, somapilha(caixas))

