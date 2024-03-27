# Descritivo do desafio

## Objetivo:
O objetivo desta etapa do desafio é complementar os dados existentes sobre Filmes e Séries, previamente carregados na Etapa 1, com informações adicionais provenientes da **API** do *The Movie Database* (**TMDB**). O propósito é enriquecer os dados já existentes com novas informações relevantes. O processo de complementação dos dados será realizado por meio de chamadas de **API** gerenciadas pela **AWS Lambda**, garantindo a escalabilidade e eficiência na obtenção e armazenamento dessas informações.   

Para a minha análise, serão avaliados dados referentes aos filmes do gêmero crime, estrelados pelo ator Robert de Niro e dirigidos por Martin Scorsese. Na fase atual, o intuito é de ingerir os dados provenientes do **TMDB**. Posteriormente, serão realizadas análises referentes aos desempenhos dos filmes e relativas entre orçamento e recepção pelo público, por exemplo.

## Endpoints Utilizados:

### TMDB API (The Movie Database)
A escolha dos endpoints da **API** do **TMDB** é fundamental para garantir que as informações complementares obtidas sejam relevantes e enriqueçam adequadamente os dados existentes sobre filmes. Foi selecionado o endpoint [*Details*](https://developer.themoviedb.org/reference/movie-details), que permitiu a realização da busca dos dados necessários.