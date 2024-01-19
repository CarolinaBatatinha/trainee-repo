# Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
# Lembre-se que você deverá desenvolver o cálculo que identifica se um número é 
# primo ou não.

# Importante: Aplique a função range().

for num in range(2, 101):
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)