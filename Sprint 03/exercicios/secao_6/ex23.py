# Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, 
# e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, 
# que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados 
# negativos são permitidos).

# Utilize os valores abaixo para testar seu exercício:

# x = 4 
# y = 5
# imprima:

# Somando: 4+5 = 9
# Subtraindo: 4-5 = -1

class Calculo:
    def somar(self, x, y):
        resultado = x + y
        return resultado

    def subtrair(self, x, y):
        resultado = x - y
        return resultado

x = 4
y = 5

calculo = Calculo()

soma_resultado = calculo.somar(x, y)
print(f'Somando: {x}+{y} = {soma_resultado}')

subtracao_resultado = calculo.subtrair(x, y)
print(f'Subtraindo: {x}-{y} = {subtracao_resultado}')
