-- Apresente a query para listar todos os livros publicados após 2014. 
-- Ordenar pela coluna cod,em ordem crescente, as linhas.
-- Atenção às colunas esperadas no resultado final: 
-- cod, titulo, autor, editora, valor, publicacao, edicao, idioma

select * 
from livro

where livro.publicacao > '2014-01-01'
order by livro.cod asc