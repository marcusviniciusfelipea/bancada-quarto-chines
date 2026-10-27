from django.test import TestCase

# Create your tests here.

from types import SimpleNamespace

from django.test import SimpleTestCase

from .estrategias import igualdade_exata, normalizacao, normalizar

# Regras "de mentira", só para os testes (não usam o banco)
R01 = SimpleNamespace(nome="R01", pergunta="Qual é o horário de funcionamento?")
R02 = SimpleNamespace(nome="R02", pergunta="Qual o horário da biblioteca?")
REGRAS = [R01, R02]


class NormalizarTeste(SimpleTestCase):
    def test_remove_maiusculas_acentos_e_pontuacao(self):
        self.assertEqual(normalizar("Qual É o HORÁRIO?"), "qual e o horario")

    def test_reduz_espacos(self):
        self.assertEqual(normalizar("  qual   o  horario "), "qual o horario")


class IgualdadeExataTeste(SimpleTestCase):
    def test_texto_identico(self):
        self.assertEqual(igualdade_exata("Qual é o horário de funcionamento?", REGRAS), R01)

    def test_minusculas_nao_casam(self):
        self.assertIsNone(igualdade_exata("qual é o horário de funcionamento?", REGRAS))


class NormalizacaoTeste(SimpleTestCase):
    def test_forma_diferente_casa(self):
        self.assertEqual(normalizacao("QUAL E O HORARIO DE FUNCIONAMENTO", REGRAS), R01)

    def test_palavras_diferentes_nao_casam(self):
        self.assertIsNone(normalizacao("Qual o horário de funcionamento?", REGRAS))