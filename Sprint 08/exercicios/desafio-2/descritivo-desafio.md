# Descritivo do desafio

## Objetivo:
O objetivo desta etapa do desafio é complementar os dados existentes sobre Filmes e Séries, previamente carregados na Etapa 1, com informações adicionais provenientes da **API** do *The Movie Database* (**TMDB**). O propósito é enriquecer os dados já existentes com novas informações relevantes. O processo de complementação dos dados será realizado por meio de chamadas de **API** gerenciadas pela **AWS Lambda**, garantindo a escalabilidade e eficiência na obtenção e armazenamento dessas informações.

## Endpoints Utilizados:

### TMDB API (The Movie Database)
A escolha dos endpoints da **API** do **TMDB** é fundamental para garantir que as informações complementares obtidas sejam relevantes e enriqueçam adequadamente os dados existentes sobre filmes. A seguir, está detalhada a seleção dos endpoints e como eles contribuem para atender aos objetivos do desafio:
  
  * [**Keywords**](https://developer.themoviedb.org/reference/movie-keywords): Essas palavras-chave podem incluir termos descritivos, temas, gêneros e outros atributos relevantes que ajudam a categorizar e identificar o conteúdo do filme.  
  * [**Popular:**](https://api.themoviedb.org/3/movie/popular): fornece informações sobre os filmes mais populares atualmente. Ao acessar este endpoint, os desenvolvedores podem obter uma lista dos filmes que estão gerando mais interesse e engajamento entre os usuários da plataforma.  
  * [**Countries:**](https://developer.themoviedb.org/reference/configuration-countries): oferece informações sobre os países associados a um filme, como locais de produção, distribuição e locações de filmagem. 