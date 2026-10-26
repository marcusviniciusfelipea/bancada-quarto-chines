"""Estratégias de casamento sintático.

Todas recebem a mensagem do usuário e a lista de regras, e devolvem
a regra escolhida ou None (quando nenhuma regra se aplica).
"""
import string
import unicodedata
from difflib import SequenceMatcher


def igualdade_exata(mensagem, regras):
    """Estratégia 1: a mensagem precisa ser idêntica à pergunta da regra."""
    for regra in regras:
        if mensagem == regra.pergunta:
            return regra
    return None

def normalizar(texto):
    """Minúsculas, sem acentos, sem pontuação e sem espaços repetidos."""
    texto = texto.lower()
    # Separa as letras dos acentos ("á" vira "a" + acento) e descarta os acentos
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    # Troca cada sinal de pontuação por um espaço
    for sinal in string.punctuation:
        texto = texto.replace(sinal, " ")
    # split() quebra nos espaços (quantos forem); join() junta com um só
    return " ".join(texto.split())


def normalizacao(mensagem, regras):
    """Estratégia 2: igualdade exata, mas entre os textos normalizados."""
    mensagem_normalizada = normalizar(mensagem)
    for regra in regras:
        if mensagem_normalizada == normalizar(regra.pergunta):
            return regra
    return None