# Protocolo do experimento

Data de congelamento: __/10/2026

## Livro de regras
- 12 regras, em dados/regras.json.
- Ordem de consulta: pelo nome (R01, R02, ...). Em caso de empate, vence a primeira.

## Bateria
- 100 mensagens, em dados/bateria.csv (categorias: identica 12, forma 20,
  parafrase 36, digitacao 12, fora 20).

## Classificação
- Adequada: regra escolhida = regra esperada.
- Inadequada: escolheu uma regra diferente da esperada, ou escolheu uma regra
  quando a esperada era nenhuma.
- Sem resposta: nenhuma regra escolhida.

## Parâmetros das estratégias (fixos)
- Normalização: minúsculas; remoção de acentos; pontuação trocada por espaço;
  espaços repetidos reduzidos a um.
- Contém: o trecho da regra aparece na mensagem, ignorando maiúsculas e minúsculas.
- Palavras-chave: a regra dispara quando pelo menos 50% das suas palavras-chave
  aparecem na mensagem normalizada; vence a regra com o maior percentual.
- Similaridade: SequenceMatcher sobre os textos normalizados; limiar = 0,75;
  vence a regra com a maior similaridade.

## Medição de tempo
- Bateria inteira executada 10 vezes por estratégia; registra-se a média.
- O tempo não inclui a leitura do banco nem do CSV.
- Computador: (ver docs/ambiente.md).