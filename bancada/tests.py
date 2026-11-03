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


R03 = SimpleNamespace(
    nome="R03",
    pergunta="Qual é o horário de funcionamento do campus?",
    trecho="funcionamento",
    palavras_chave="horario, funcionamento, campus",
)

R05 = SimpleNamespace(
    nome="R05",
    pergunta="qual o horario que o refeitorio abre para a merenda",
    trecho="refeitorio",
    palavras_chave="horario, refeitorio, merenda",
)

R07 = SimpleNamespace(
    nome="R07",
    pergunta="Que horas o ônibus sai do campus no final da tarde?",
    trecho="onibus",
    palavras_chave="horas, ônibus, tarde",
)

R08 = SimpleNamespace(
    nome="R08",
    pergunta="Que horas os funcionários e servidores encerram o turno?",
    trecho="funcionarios",
    palavras_chave="horas, servidores, turno",
)

R08 = SimpleNamespace(
    nome="R08",
    pergunta="Qual o horaro que a maioria dos servidres acabam o turno",
    trecho="horário",
    palavras_chave="De quantas horas a maioria dos servidores vão para casa?",
)

R012 = SimpleNamespace(
    nome="R012",
    pergunta="Quais os auxilios q o campus disponibiliza aos alunos",
    trecho="auxílios",
    palavras_chave="O campus oferece quais tipos de auxilios aos alunos",
)

R04 = SimpleNamespace(
    nome="R04",
    pergunta="O que signific os dois ultimos numros da matricla",
    trecho="últimos",
    palavras_chave="Qual o significado dos últimos dois números da matrícula?",
)