# Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada 
# Passaro as habilidades de voar e emitir som.
# Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita)
# no console, conforme o modelo a seguir.

# Imprima no console exatamente assim:

# Pato
# Voando...
# Pato emitindo som...
# Quack Quack
# Pardal
# Voando...
# Pardal emitindo som...
# Piu Piu

class Passaro:
    
    def __init__(self,nome):
        self.nome = nome
    def voar(self):
        print('Voando...')

    def emitir_som(self):
        print(f'{self.nome} emitindo som...')


class Pato(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print('Quack Quack')


class Pardal(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print('Piu Piu')


pato = Pato('Pato')
print('Pato')
pato.voar()
pato.emitir_som()

pardal = Pardal('Pardal')
print('Pardal')
pardal.voar()
pardal.emitir_som()
