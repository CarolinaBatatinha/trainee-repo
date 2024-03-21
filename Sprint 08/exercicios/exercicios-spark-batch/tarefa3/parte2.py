# 2)  Em Python, declare e inicialize uma lista contendo o nome de 20 animais. Ordene-os em ordem crescente e itere sobre os itens, imprimindo um a um (você pode utilizar list comprehension aqui).  Na sequência, armazene o conteúdo da lista em um arquivo de texto, um item em cada linha, no formato CSV.

import csv

animais = ['cachorro', 'gato', 'cavalo', 'coelho', 'abelha', 'tubarão', 'gorila', 'esquilo', 'capivara', 'baleia', 'arara', 'vaca', 'cabra', 'porco', 'leão', 'girafa', 'rinoceronte', 'pato', 'carneiro', 'tamanduá']

animais_ordenados = sorted(animais)

print('Nome dos animais em ordem crescente: ')
[print(animal) for animal in animais_ordenados]

nome_arquivo = f'nome_animais.csv'

with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerows([[animal] for animal in animais_ordenados])

print(f'\nO conteúdo foi armazenado no arquivo CSV: {nome_arquivo}')
