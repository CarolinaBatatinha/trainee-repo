-- Apresente a query para listar a quantidade de livros publicada por cada autor. 
-- Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
-- Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

select 
    autor.codautor,
    autor.nome,
    autor.nascimento,
    count(livro.cod) as quantidade
from autor
left join livro on autor.codautor = livro.autor

group by autor.codautor, autor.nome, autor.nascimento
order by autor.nome