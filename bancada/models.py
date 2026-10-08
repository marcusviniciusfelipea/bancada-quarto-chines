from django.db import models

# Create your models here.


class Regra(models.Model):
    # Identificação curta, usada no gabarito (ex.: R01)
    nome = models.CharField(max_length=10, unique=True)
    # Assunto, só para você se localizar (ex.: "Horário do campus")
    assunto = models.CharField(max_length=100)
    # Pergunta cadastrada: usada pelas estratégias 1, 2 e 5
    pergunta = models.CharField(max_length=200)
    # Trecho curto: usado pela estratégia 3 (contém)
    trecho = models.CharField(max_length=50)
    # Palavras-chave separadas por vírgula: usadas pela estratégia 4
    palavras_chave = models.CharField(max_length=200)
    # Resposta que o sistema devolve quando a regra é escolhida
    resposta = models.TextField()

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.assunto}"


