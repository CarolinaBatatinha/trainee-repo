# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

# Dica: leia a documentação do pacote json

import json

nome_arquivo = 'person.json'

with open(nome_arquivo, 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)
