import unittest

def somapilha(caixas):
    if len(caixas) == 2:
        if caixas[1][1] >= caixas[0][1]:
            return caixas[0][0] + caixas[1][0]
        else:
            return caixas[0][0] + (caixas[1][0] - caixas[0][0])
    else:
        return caixas[0][0]

def somapilha2(caixas):
    altura = 0
    ultima_largura = 0
    for caixa in caixas:
        if ultima_largura <= caixa[1]:
            altura = altura + caixa[0]

        ultima_largura = caixa[1]
    return altura

class DojoTest(unittest.TestCase):

    def test_uma_caixa(self):
        caixas = [(10,15)]
        self.assertEquals(10, somapilha(caixas))

    def test_dois_caixa(self):
        caixas = [(10,15),(15,5)]
        self.assertEquals(15, somapilha(caixas))
