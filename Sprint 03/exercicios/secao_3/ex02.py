# Escreva um código Python para verificar se três números digitados na entrada padrão são 
# pares ou ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente 
# (um linha para cada número lido).

# Importante: Aplique a função range() em seu código.

# Exemplos de saída:

# Par: 2
# Ímpar: 3

for i in range(3):
    num = int(input('Digite um número: '))
    
    if num % 2 == 0:
        print(f'Par: {num}')
    else:
        print(f'Ímpar: {num}')