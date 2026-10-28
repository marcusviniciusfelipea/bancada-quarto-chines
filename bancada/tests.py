
from types import SimpleNamespace
from django.test import SimpleTestCase

from .estrategias import igualdade_exata, normalizacao, normalizar


# Regras fictícias utilizadas somente nos testes.
# Não dependem do banco de dados.
R01 = SimpleNamespace(
    nome="R01",
    pergunta="Qual é o horário de funcionamento?"
)

R02 = SimpleNamespace(
    nome="R02",
    pergunta="Qual o horário da biblioteca?"
)

REGRAS = [R01, R02]


class NormalizarTeste(SimpleTestCase):
    """Testes da função responsável por normalizar textos."""

    def test_remove_maiusculas_acentos_e_pontuacao(self):
        self.assertEqual(
            normalizar("Qual É o HORÁRIO?"),
            "qual e o horario"
        )

    def test_reduz_espacos_repetidos(self):
        self.assertEqual(
            normalizar("  qual   o  horario "),
            "qual o horario"
        )


class IgualdadeExataTeste(SimpleTestCase):
    """Testes da estratégia de igualdade exata."""

    def test_texto_identico(self):
        self.assertEqual(
            igualdade_exata(
                "Qual é o horário de funcionamento?",
                REGRAS
            ),
            R01
        )

    def test_minusculas_nao_casam(self):
        self.assertIsNone(
            igualdade_exata(
                "qual é o horário de funcionamento?",
                REGRAS
            )
        )

    def test_igualdade_exata_outra_pergunta(self):
        self.assertEqual(
            igualdade_exata(
                "Qual o horário da biblioteca?",
                REGRAS
            ),
            R02
        )

    def test_igualdade_exata_texto_diferente(self):
        self.assertIsNone(
            igualdade_exata(
                "Qual o horário de funcionamento?",
                REGRAS
            )
        )


class NormalizacaoTeste(SimpleTestCase):
    """Testes da estratégia de igualdade após normalização."""

    def test_forma_diferente_casa(self):
        self.assertEqual(
            normalizacao(
                "QUAL E O HORARIO DE FUNCIONAMENTO",
                REGRAS
            ),
            R01
        )

    def test_palavras_diferentes_nao_casam(self):
        self.assertIsNone(
            normalizacao(
                "Qual o horário de funcionamento?",
                REGRAS
            )
        )

    def test_normalizacao_ignora_pontuacao(self):
        self.assertEqual(
            normalizacao(
                "QUAL É O HORÁRIO DE FUNCIONAMENTO!",
                REGRAS
            ),
            R01
        )

    def test_normalizacao_ignora_espacos(self):
        self.assertEqual(
            normalizacao(
                "  Qual   é o horário de funcionamento?  ",
                REGRAS
            ),
            R01
        )
