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

def contem(mensagem, regras):
    """Estratégia 3: o trecho da regra aparece na mensagem (ignora maiúsculas)."""
    mensagem_minuscula = mensagem.lower()
    for regra in regras:
        if regra.trecho.lower() in mensagem_minuscula:
            return regra
    return None 

PROPORCAO_MINIMA_PALAVRAS_CHAVE = 0.5


def palavras_chave(mensagem, regras):
    """Estratégia 4: pelo menos 50% das palavras-chave aparecem na mensagem.

    Vence a regra com o maior percentual; em caso de empate, a primeira.
    """
    palavras_da_mensagem = set(normalizar(mensagem).split())
    melhor_regra = None
    maior_proporcao = 0.0
    for regra in regras:
        chaves = [normalizar(p) for p in regra.palavras_chave.split(",") if p.strip()]
        if not chaves:
            continue
        encontradas = sum(1 for chave in chaves if chave in palavras_da_mensagem)
        proporcao = encontradas / len(chaves)
        if proporcao > maior_proporcao:
            melhor_regra = regra
            maior_proporcao = proporcao
    if maior_proporcao >= PROPORCAO_MINIMA_PALAVRAS_CHAVE:
        return melhor_regra
    return None

LIMIAR_SIMILARIDADE = 0.75


def similaridade(mensagem, regras):
    """Estratégia 5: a regra com a pergunta mais parecida, se passar do limiar."""
    mensagem_normalizada = normalizar(mensagem)
    melhor_regra = None
    maior_valor = 0.0
    for regra in regras:
        valor = SequenceMatcher(None, mensagem_normalizada, normalizar(regra.pergunta)).ratio()
        if valor > maior_valor:
            melhor_regra = regra
            maior_valor = valor
    if maior_valor >= LIMIAR_SIMILARIDADE:
        return melhor_regra
    return None


# Todas as estratégias, na ordem em que aparecem no TCC
ESTRATEGIAS = {
    "Igualdade exata": igualdade_exata,
    "Normalização": normalizacao,
    "Contém": contem,
    "Palavras-chave": palavras_chave,
    "Similaridade": similaridade,
}