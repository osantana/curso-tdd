import unittest

def somapilha(caixas):

    alt_ant = 0
    lrg_ant = 0
    result = 0

    for altura, largura in caixas:
        if largura >= lrg_ant:
            result += altura
        else:
            result += max(0,(altura - alt_ant))

        lrg_ant = largura
        alt_ant = altura
    return result


class DojoTest(unittest.TestCase):

    def test_uma_caixa(self):
        caixas = [(10,15)]
        self.assertEquals(10, somapilha(caixas))

    def test_duas_caixas(self):
        caixas = [(10,15),(15,5)]
        self.assertEquals(15, somapilha(caixas))

    def test_tres_caixas(self):
        caixas = [(10,15),(15,5),(8,7)]
        self.assertEquals(23, somapilha(caixas))

    def test_quatro_caixas(self):
        caixas = [(10,15),(15,5),(8,7),(5,3)]
        self.assertEquals(23, somapilha(caixas))

    def test_cinco_caixas(self):
        caixas = [(10,15),(15,5),(8,7),(50,1)]
        self.assertEquals(65, somapilha(caixas))
