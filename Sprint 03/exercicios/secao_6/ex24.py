# Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha
# os métodos ordenacaoCrescente e ordenacaoDecrescente.
# Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como 
# listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto, decrescente dessa 
# mesma classe com uma outra listaBaguncada sendo [9,7,6,8].

# Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo 
# objeto, use o método ordenacaoDecrescente.

# Imprima o resultado da ordenação crescente e da ordenação decresce

# [1, 2, 3, 4, 5] 
# [9, 8, 7, 6]

class Ordenadora:
    def __init__(self, lista_baguncada):
        self.listaBaguncada = lista_baguncada

    def ordenacaoCrescente(self):
        self.listaBaguncada.sort()

    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort(reverse=True)
        return self.listaBaguncada

crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

crescente.ordenacaoCrescente()
decrescente.ordenacaoDecrescente()

print(crescente.listaBaguncada)
print(decrescente.listaBaguncada)
