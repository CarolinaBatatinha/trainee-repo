# Utilizando high order functions, implemente o corpo da função conta_vogais.
# O parâmetro de entrada será uma string e o resultado deverá ser a contagem 
# de vogais presentes em seu conteúdo.

# É obrigatório aplicar as seguintes funções:

# len
# filter
# lambda

# Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do 
# seu código.

def conta_vogais(s):
    is_vogal = lambda x: x.lower() in 'aeiou'
    vogais = list(filter(is_vogal, s))
    return len(vogais)


texto = "Olá, isso é um exemplo de string com vogais."
resultado = conta_vogais(texto)
print(f"A quantidade de vogais no texto é: {resultado}")
