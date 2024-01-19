# Dada as listas a seguir:

# primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
# sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
# idades = [19, 28, 25, 31]

# Faça um programa que imprima os dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".

# Exemplo:
# 0 - João Soares está com 19 anos

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, primeiroNome in enumerate(primeirosNomes):
    sobreNome = sobreNomes[indice]
    idade = idades[indice]

    print(f'{indice} - {primeiroNome} {sobreNome} está com {idade} anos')

