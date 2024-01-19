# 1 - Apresente o ator/atriz com maior número de filmes e a respectiva quantidade. A quantidade de filmes encontra-se na coluna Number of Movies do arquivo.

ator_max_filmes = ''
quantidade_max_filmes = 0

caminho_arquivo_csv = 'actors.csv'
with open(caminho_arquivo_csv, 'r', encoding='utf-8') as arquivo_csv:

    linhas = arquivo_csv.readlines()

    for linha in linhas [1:]:
        colunas = linha.strip().split(',')

        nome_ator = colunas[0]
        quantidade_filmes = int(colunas[-4])
        if quantidade_filmes > quantidade_max_filmes:
            ator_max_filmes = nome_ator
            quantidade_max_filmes = quantidade_filmes

with open('etapa-1.txt', 'w') as arquivo1_saida:
    arquivo1_saida.write(f'O ator/atriz com maior número de filmes é {ator_max_filmes} com {quantidade_max_filmes} filmes.')


# 2 - Apresente a média de receita de bilheteria bruta dos principais filmes, considerando todos os atores. Estamos falando aqui da média da coluna Gross.

with open('actors.csv', 'r', encoding='utf-8') as arquivo2:
    linhas = arquivo2.readlines()

receitas_brutas = []

for linha in linhas[1:]:
    data = linha.strip().split(',')

    gross = float(data[-1])

    receitas_brutas.append(gross)

media_receitas_brutas = sum(receitas_brutas) / len(receitas_brutas)

with open('etapa-2.txt', 'w', encoding='utf-8') as arquivo2_saida:
    arquivo2_saida.write(f'Média de receita de bilheteria bruta dos principais filmes: {media_receitas_brutas:.2f} milhões de dólares')

# 3 - Apresente o ator/atriz com a maior média de receita de bilheteria bruta por filme do conjunto de dados. 
# Considere a coluna Avarage per Movie para fins de cálculo.

with open('actors.csv', 'r', encoding='utf-8') as arquivo3:
    linhas = arquivo3.readlines()

media_por_filme_por_ator = {}

for linha in linhas[1:]:
    data = linha.strip().split(',')

    ator = data[0]
    media_por_filme = float(data[3])

    media_por_filme_por_ator[ator] = media_por_filme

ator_maior_media = max(media_por_filme_por_ator, key=media_por_filme_por_ator.get)
maior_media = media_por_filme_por_ator[ator_maior_media]

with open('etapa-3.txt', 'w', encoding='utf-8') as arquivo3_saida:
    arquivo3_saida.write(f'{ator_maior_media} - Maior média de receita por filme: {maior_media:.2f} milhões de dólares')
    

# 4 - A coluna #1 Movie contém o filme de maior bilheteria em que o ator atuou. Realize a contagem de aparições 
# destes filmes no dataset, listando-os ordenados pela quantidade de vezes em que estão presentes. Considere a 
# ordem decrescente e, em segundo nível, o nome do filme.

# Ao escrever no arquivo, considere o padrão de saída <sequencia> - O filme <nome filme> aparece <quantidade> 
# vez(es) no dataset, adicionando um resultado a cada linha.

with open('actors.csv', 'r', encoding='utf-8') as arquivo4:
    linhas = arquivo4.readlines()

contagem_filmes = {}

for linha in linhas[1:]:
    filme = linha.strip().split(',')[-2]

    contagem_filmes[filme] = contagem_filmes.get(filme, 0) + 1

def ordenar(item):
    return (item[1], item[0])

contagem_filmes_ordenada = sorted(contagem_filmes.items(), key=ordenar, reverse=True)

with open('etapa-4.txt', 'w', encoding='utf-8') as arquivo4_saida:
    sequencia = 1
    for filme, quantidade in contagem_filmes_ordenada:
        arquivo4_saida.write(f'{sequencia} - O filme {filme} aparece {quantidade} vez(es) no dataset.\n')
        sequencia += 1
        

# 5 - Apresente a lista dos atores ordenada pela receita bruta de bilheteria de seus filmes (coluna Total Gross),
# em ordem decrescente.

# Ao escrever no arquivo, considere o padrão de saída <nome do ator> -  <receita total bruta>, adicionando um resultado a cada linha.

def processar_linha(linha):
    elementos_processados = []
    dentro_de_string = False
    elemento_atual = ''

    for caractere in linha:
        if caractere == ',' and not dentro_de_string:
            elementos_processados.append(elemento_atual)
            elemento_atual = ''
        elif caractere == '"':
            dentro_de_string = not dentro_de_string
        else:
            elemento_atual += caractere

    elementos_processados.append(elemento_atual.strip())
    return elementos_processados

def chave_ordenacao(linha):
    return float(processar_linha(linha)[1])

linhas_processadas = []

with open('actors.csv', 'r') as arquivo_entrada:
    lines = arquivo_entrada.readlines()

linhas_ordenadas = sorted(lines[1:], key=chave_ordenacao, reverse=True)

for linha in linhas_ordenadas:
    elementos_linha = processar_linha(linha)
    nome_ator, receita_total_bruta = elementos_linha[0], float(elementos_linha[1])
    nova_linha = f'{nome_ator} - {receita_total_bruta} milhões de dólares\n'
    linhas_processadas.append(nova_linha)

with open('etapa-5.txt', 'w') as arquivo5_saida:
    for linha_processada in linhas_processadas:
        arquivo5_saida.write(linha_processada)
