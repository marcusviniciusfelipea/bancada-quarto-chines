import csv
import time
from pathlib import Path

from django.core.management.base import BaseCommand

from bancada.estrategias import ESTRATEGIAS
from bancada.models import Regra

ARQUIVO_BATERIA = Path("dados/bateria.csv")
PASTA_RESULTADOS = Path("resultados")
REPETICOES_TEMPO = 10


def classificar(regra_esperada, regra_obtida):
    """Compara o que a estratégia escolheu com o gabarito."""
    if regra_obtida == "":
        return "sem resposta"
    if regra_obtida == regra_esperada:
        return "adequada"
    return "inadequada"


class Command(BaseCommand):
    help = "Executa a bateria de mensagens em todas as estratégias e grava os resultados."

    def handle(self, *args, **options):
        # Lê o livro de regras e a bateria UMA vez, fora da medição de tempo
        regras = list(Regra.objects.order_by("nome"))
        with open(ARQUIVO_BATERIA, encoding="utf-8-sig", newline="") as arquivo:
            bateria = list(csv.DictReader(arquivo))
        self.stdout.write(f"{len(regras)} regras e {len(bateria)} mensagens carregadas.")

        PASTA_RESULTADOS.mkdir(exist_ok=True)
        detalhes = []
        resumo = []

        for nome_estrategia, estrategia in ESTRATEGIAS.items():
            contagem = {"adequada": 0, "inadequada": 0, "sem resposta": 0}
            silencio_correto = 0

            # 1) Classificação: cada mensagem passa uma vez pela estratégia
            for item in bateria:
                esperada = item["regra_esperada"].strip()
                regra = estrategia(item["mensagem"], regras)
                obtida = regra.nome if regra else ""
                classificacao = classificar(esperada, obtida)
                contagem[classificacao] += 1
                if classificacao == "sem resposta" and esperada == "":
                    silencio_correto += 1
                detalhes.append({
                    "estrategia": nome_estrategia,
                    "numero": item["numero"],
                    "mensagem": item["mensagem"],
                    "categoria": item["categoria"],
                    "regra_esperada": esperada,
                    "regra_obtida": obtida,
                    "classificacao": classificacao,
                })

            # 2) Tempo: a bateria inteira, repetida várias vezes
            tempos = []
            for _ in range(REPETICOES_TEMPO):
                inicio = time.perf_counter()
                for item in bateria:
                    estrategia(item["mensagem"], regras)
                tempos.append(time.perf_counter() - inicio)
            tempo_medio_ms = sum(tempos) / len(tempos) * 1000

            resumo.append({
                "estrategia": nome_estrategia,
                "adequadas": contagem["adequada"],
                "inadequadas": contagem["inadequada"],
                "sem_resposta": contagem["sem resposta"],
                "sem_resposta_correta": silencio_correto,
                "tempo_medio_ms": f"{tempo_medio_ms:.3f}",
            })
            self.stdout.write(
                f"{nome_estrategia:<16} adequadas={contagem['adequada']:>3} "
                f"inadequadas={contagem['inadequada']:>3} "
                f"sem resposta={contagem['sem resposta']:>3} "
                f"tempo={tempo_medio_ms:.3f} ms"
            )

        self.gravar_csv(PASTA_RESULTADOS / "detalhado.csv", detalhes)
        self.gravar_csv(PASTA_RESULTADOS / "resumo.csv", resumo)
        self.stdout.write(self.style.SUCCESS("Resultados gravados na pasta resultados/."))

    def gravar_csv(self, caminho, linhas):
        with open(caminho, "w", encoding="utf-8-sig", newline="") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=linhas[0].keys())
            escritor.writeheader()
            escritor.writerows(linhas)