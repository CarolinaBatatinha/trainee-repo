# Leia o arquivo actors.csv e codifique os cálculos solicitados sobre o conjunto de dados utilizando a biblioteca Pandas.
# Adicione apenas a resposta da questões nos espaços indicados. Seu código-fonte deverá estar no Github.

# Perguntas dessa tarefa

# 1 - Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.

import pandas as pd

df = pd.read_csv('actors.csv')

ator_maior_numero_filmes = df.loc[df['Number of Movies'].idxmax()]
nome_ator_maior_numero_filmes = ator_maior_numero_filmes['Actor']
numero_filmes_max = ator_maior_numero_filmes['Number of Movies']

print(f"Ator/atriz com o maior número de filmes: {nome_ator_maior_numero_filmes} com {numero_filmes_max} filmes")

# 2 - Apresente a média da coluna contendo o número de filmes.

media_numero_filmes = df['Number of Movies'].mean()
print(f"Média da coluna 'Number of Movies': {media_numero_filmes:.2f}")

# 3 - Apresente o nome do ator/atriz com a maior média por número de filmes.

# Encontrar o ator/atriz com a maior média
ator_maior_media = df.loc[df['Average per Movie'].idxmax()]['Actor']
maior_media_por_filme = df['Average per Movie'].max()

# Exibir o resultado
print(f"Ator/atrizes com a maior média por filme: {ator_maior_media} com média de {maior_media_por_filme:.2f}")

# 4 - Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

# Encontrar o(s) filme(s) mais frequente(s) e sua respectiva frequência
filme_mais_frequente = df['#1 Movie'].mode()
frequencia_filme_mais_frequente = df['#1 Movie'].value_counts().max()

print(f"Filme(s) mais frequente(s): {', '.join(filme_mais_frequente)} com frequência de {frequencia_filme_mais_frequente} vez(es)")


