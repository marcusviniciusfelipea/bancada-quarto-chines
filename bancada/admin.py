from django.contrib import admin

from .models import Regra


@admin.register(Regra)
class RegraAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "pergunta", "trecho", "palavras_chave"]
    search_fields = ["nome", "assunto", "pergunta"]


