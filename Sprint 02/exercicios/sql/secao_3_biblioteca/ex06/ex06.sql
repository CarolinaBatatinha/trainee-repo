-- Apresente a query para listar o autor com maior número de livros publicados. 
-- O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

select
    autor.codautor,
    autor.nome,
    count(livro.cod) AS quantidade_publicacoes
from autor
join livro on autor.codautor = livro.autor

group by autor.codautor, autor.nome
order by quantidade_publicacoes desc
limit 1