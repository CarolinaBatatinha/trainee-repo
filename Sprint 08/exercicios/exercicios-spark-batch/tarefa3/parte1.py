# 1) [Warm up] Em Python, declare e inicialize uma lista contendo 250 inteiros obtidos de forma aleatória. Após, aplicar o método reverse sobre o conteúdo da lista e imprimir o resultado.

import random

def gerar_lista_aleatoria():
    return [random.randint(1, 1000) for _ in range(250)]

def imprimir_lista_invertida(lista):
    print('\nLista original: \n')
    print(lista)
    
    lista.reverse()
    
    print('\nLista no modo reverse: \n')
    print(lista)

lista_aleatoria = gerar_lista_aleatoria()

imprimir_lista_invertida(lista_aleatoria)
