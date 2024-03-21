
# 3) [Laboratório] Elaborar um código Python para gerar um dataset de nomes de pessoas. 

import random
import names

random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

print(f'Gerando {qtd_nomes_aleatorios} nomes aleatórios')

dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]

nome_arquivo = 'nomes_aleatorios.txt'

with open(nome_arquivo, 'w') as arquivo:
    for nome in dados:
        arquivo.write(nome + '\n')

with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()

print('Conteúdo do arquivo: ')
print(conteudo)