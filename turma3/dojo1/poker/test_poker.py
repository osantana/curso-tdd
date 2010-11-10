import unittest

def compare(c1, c2):
    (num1, naipe1) = c1
    (num2, naipe2) = c2

    cartas = "23456789TJQKA"
    index1 = cartas.index( num1 )
    index2 = cartas.index( num2 )

    if index1 > index2:
        return 1
    elif index1 < index2:
        return -1
    else:
        return 0

def get_lista(mao, qtd):
    n = []
    for c1 in mao:
        if n.count(c1[0])==qtd-1:
            return c1[0]+"X"
        n.append(c1[0])

PAR = 2
TRINCA = 3

def get_par(mao):
    return get_lista( mao, PAR )

def get_trinca(mao):
    return get_lista( mao, TRINCA )

def get_quadra(mao):
    return "JX"

class TestPoker(unittest.TestCase):
    def test_compare_card_3c_2c_returns_1(self):
        self.assertEquals(1, compare("3C", "2C"))

    def test_compare_card_2c_3c_returns_minus_1(self):
        self.assertEquals(-1, compare("2C", "3C"))

    def test_compare_card_2c_2o_returns_0(self):
        self.assertEquals(0, compare("2C", "2O"))

    def test_compare_card_ac_jo_returns_1(self):
        self.assertEquals(1, compare("AC", "JO"))

    def test_compare_card_qc_ko_returns_minus_1(self):
        self.assertEquals(-1, compare("QC", "KO"))

    def test_compare_card_jp_je_returns_0(self):
        self.assertEquals(0, compare("JP", "JE"))

    def test_compare_card_qp_qe_returns_0(self):
        self.assertEquals(0, compare("QP", "QE"))

    def test_dez(self):
        self.assertEquals(1, compare("TC","9O"))

    def test_obtem_par_de_uma_mao(self):
        mao1 = ["2C","2O", "3C", "5P", "6C" ]
        self.assertEquals("2X", get_par(mao1))

    def test_obtem_par_diferente_de_2C(self):
        mao1 = ["2O","2C", "3C", "5P", "6C" ]
        self.assertEquals("2X",get_par(mao1))

    def test_obtem_par_independe_posicao(self):
        mao1 = [ "3C","2C","2O", "5P", "6C" ]
        self.assertEquals("2X",get_par(mao1))

    def test_obtem_par_com_carta_maior(self):
        mao1 = ["3C", "2C", "5P", "5O", "6C" ]
        self.assertEquals("5X", get_par(mao1))

    def test_mao_sem_par(self):
        mao1 = ["3C", "2C", "5P", "7O", "6C" ]
        self.assertEquals(None, get_par(mao1))

    def test_obtem_par_JO_JC(self):
        mao1 = ["3C", "2C", "JO", "JC", "6C" ]
        self.assertEquals("JX", get_par(mao1))

    def test_obtem_par_KO_KC(self):
        mao1 = ["KC", "2C", "3O", "JC", "KO" ]
        self.assertEquals("KX", get_par(mao1))

    def test_obtem_trinca_with_1(self):
        mao1 = ["1C", "1O", "1P", "JC", "6C" ]
        self.assertEquals("1X", get_trinca(mao1))

    def test_sem_trinca(self):
        mao1 = ["2C", "1O", "1P", "JC", "6C" ]
        self.assertEquals(None, get_trinca(mao1))

    def test_obtem_trinca_com_1_separado(self):
        mao1 = ["JC", "1O", "JO", "1C", "1P" ]
        self.assertEquals("1X", get_trinca(mao1))

    def test_obtem_quadra_de_J(self):
        mao1 = ["JC", "JP", "JE", "JO", "3C"]
        self.assertEquals("JX", get_quadra(mao1))

    def test_sem_quadra(self):
        mao1 = ["JC", "1O", "JO", "1C", "1P" ]
        self.assertEquals(None, get_quadra(mao1))
