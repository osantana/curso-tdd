Test-Driven Development
=======================

.. toctree::
   :maxdepth: 2

Material de apoio
-----------------


Atividade dos algarismos romanos (slide 17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apresentação:

1. Descrever o problema (slide 18)
2. Preparar o ambiente (slide 19)
3. Mostrar as etapas de um teste (slide 20)
4. Dar as dicas (slide 21)
5. Trabalhar no terminal
6. Montar o arquivo test_roman.py::

	import unittest

	from roman import to_roman

	class TestRoman(unittest.TestCase):
	    def test_zero(self):
	        self.assertEquals("", to_roman(0))

7. Executar com unittest::

     python -m unittest test_roman

8. Executar com nose::

     nosetests

9. doctests

 * Mostrar como testar com o doctest (test_roman.txt)::

     Vamos testar o número 0::

         >>> from roman import to_roman
         >>> to_roman(0)
         ''

 * Executar com doctest::

     python -m doctest test_roman.txt

 * Executar com nose::

     nosetests --with-doctest --doctest-extension=txt

10. Voltar para slides

O problema do Roman
+++++++++++++++++++

Passos para ilustrar::

1. Testa o retorno de zero -> "" e simplesmente retorna ""
2. Testa o retorno para 1 -> "I" e coloca um if n == 1: ...
3. Testa retorno do 2 -> "II" mas usa "Triangulate" por conta de duas ou mais
   condições de retorno.
4. Implementa um concatena N vezes o caracter "I"
5. Refatora ele para uma versão recursiva
6. Faz um teste para 3 -> III
7. O teste passará de primeira... pausa, então, para explicar que neste caso
nós temos um dos seguintes casos:
 1. O teste está quebrado.
 2. O teste é desnecessário (ao menos nesse momento)
8. Neste caso podemos optar por remover o teste, mas, só devemos fazer isso se
estivermos absolutamente seguros de que o teste é desnecessário. Como não é o
meu caso, mantenho o teste.
9. Teste com 4->IV falha.
10. Implementamos um "return 'IV'"
11. Falha no caso 5->V
12. Outro caso especial pra tratar o 5->V
13. Faz o teste para VI... funciona? Não!
14. O problema é a ordem da concatenação. Então invertemos essa ordem. E funciona.
15. Reaproveita o último teste só pra mostrar que funciona com 7 e 8 também. Mas
removemos depois
16. Passamos para o número 9->IX.. e falha!
17. Adicionamos outro if para o caso 9->IX
18. Devem estar irritados/cansados, certo? Não se preocupem, estou exagerando no
tamanho dos passos para reforçar a idéia. No dia-a-dia podemos aumentar o tamanho
desses passos naturalmente. Até o momento em que chegamos à uma "red bar" que
persiste em não ficar verde. Neste caso, voltamos aos baby steps.
19. Mas vamos ver nosso código... ele está bem feio, não? Como podemos melhorar?
20. Discussões? Eu sugiro um dicionário, afinal, uma cadeia de if/elif pode ser
simulada com um dicionário, correto? Então: if n in dic: return dic[n]. Colocamos
somente os casos especiais dentro do dicionário e mantemos a concatenacao de Is.
21. Roda o teste. Reaproveitamos o teste do 10->X só para mostrar que 11, 12 e
13 funcionam corretamente e depois removemos para passar direto pro 14->IX que
falha. Falha porque estamos lidando com um número composto de 2 casos especiais:
XIV é X+IV. Colocamos o I como caso especial e vamos discutir.
22. Chegaremos à uma solução próxima do código abaixo.

Problema resolvido::

    def to_roman(decimal):
        values = (
            (1000, "M"),
            ( 900, "CM"),
            ( 500, "D"),
            ( 400, "CD"),
            ( 100, "C"),
            (  90, "XC"),
            (  50, "L"),
            (  40, "XL"),
            (  10, "X"),
            (   9, "IX"),
            (   5, "V"),
            (   4, "IV"),
            (   1, "I"),
        )

        for d, v in values:
            if decimal == d:
                return v

            if decimal > d:
                return to_roman(d) + to_roman(decimal - d)

        return ""

Características
~~~~~~~~~~~~~~~

TODO

Dependências
~~~~~~~~~~~~

Pacotes instalados:

* NoseGAE
* NoseGrowl
* Pygments
* WebOb
* WebTest
* coverage
* distribute
* mocker
* nose
* py-Growl
* rednose
* selenium
* tdaemon
* virtualenv
* wsgiref


Indices e tabelas
=================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

