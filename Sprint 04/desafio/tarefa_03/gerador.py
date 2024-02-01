import hashlib

cont = 0

while cont <= 10:

    entrada = input('Digite qualquer coisa: ')

    gerador_hash = hashlib.sha1(entrada.encode('utf-8'))

    print(gerador_hash.hexdigest())
    cont+=1
