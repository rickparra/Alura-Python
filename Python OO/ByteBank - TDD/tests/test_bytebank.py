import pytest
from pytest import mark

from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('teste', entrada, 1111)
        resultado = funcionario_teste.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_900000(self):
        entrada_salario = 100000
        esperado = 90000
        entrada_nome = 'Henrique Bragança'

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def teste_quando_calcularBonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def teste_quando_calcularBonus_recebe_100000_deve_retornar_o_exception(self):
        with pytest.raises(Exception):
            entrada = 100000


            funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
            funcionario_teste.decrescimo_salario()
            resultado = funcionario_teste.calcular_bonus()

            assert resultado

    def retorno_str(self):
        nome, data_nascimento, salario = 'teste', '12/03/2000', 1000
        esperado = f'Funcionario(teste, 12/03/2000, 1000'

        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__()

        assert resultado == esperado
