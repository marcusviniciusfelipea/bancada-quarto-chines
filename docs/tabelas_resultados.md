# Tabelas de Resultados Experimentais — Sprint 7

Este documento apresenta os resultados da execução oficial do experimento, realizada com 100 mensagens e 12 regras, utilizando cinco estratégias de correspondência.

## 1. Tabela comparativa geral

A tabela apresenta a quantidade de respostas adequadas, inadequadas e sem resposta, além do tempo médio de execução de cada estratégia.

| Estratégia | Adequadas | Inadequadas | Sem resposta | Tempo médio (ms) |
|---|---:|---:|---:|---:|
| Igualdade exata | 9 | 0 | 91 | 0,059 |
| Normalização | 22 | 0 | 78 | 13,426 |
| Contém | 19 | 0 | 81 | 0,230 |
| Palavras-chave | 54 | 6 | 40 | 18,253 |
| Similaridade | 36 | 0 | 64 | 197,103 |

## 2. Respostas adequadas por categoria

A tabela apresenta a quantidade de mensagens classificadas como adequadas por cada estratégia, considerando as cinco categorias da bateria experimental.

| Estratégia | Idêntica | Forma | Paráfrase | Digitação | Fora |
|---|---:|---:|---:|---:|---:|
| Igualdade exata | 9 | 0 | 0 | 0 | 0 |
| Normalização | 12 | 10 | 0 | 0 | 0 |
| Contém | 12 | 5 | 2 | 0 | 0 |
| Palavras-chave | 11 | 19 | 20 | 4 | 0 |
| Similaridade | 12 | 12 | 1 | 11 | 0 |

## 3. Observações sobre os resultados

A estratégia de palavras-chave apresentou o maior número de respostas adequadas, totalizando 54 mensagens. Seu desempenho se destacou principalmente nas categorias de paráfrase e variações de forma.

A estratégia de similaridade obteve 36 respostas adequadas e apresentou resultados relevantes na categoria de digitação, com 11 ocorrências. Entretanto, registrou o maior tempo médio de execução entre as estratégias avaliadas.

A igualdade exata apresentou o menor tempo médio, mas reconheceu adequadamente apenas 9 mensagens, todas da categoria idêntica.

A normalização e a estratégia Contém apresentaram resultados intermediários, demonstrando diferentes capacidades de reconhecimento de variações nas mensagens.

Nenhuma estratégia apresentou respostas adequadas na categoria fora.

## 4. Fonte dos dados

Os dados apresentados foram obtidos dos arquivos `resultados/resumo.csv` e `resultados/detalhado.csv`, gerados pela execução oficial identificada pela tag `execucao-oficial`.

Os valores desta documentação correspondem aos resultados registrados nessa execução.
