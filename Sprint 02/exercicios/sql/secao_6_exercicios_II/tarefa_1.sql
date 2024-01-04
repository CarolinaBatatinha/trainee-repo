-- Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV. 
-- Utilizar o caractere ; (ponto e vírgula) como separador. 
-- Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo:


-- CodLivro
-- Titulo
-- CodAutor
-- NomeAutor
-- Valor
-- CodEditora
-- NomeEditora

select 
    l.cod as CodLivro,
    l.titulo as Titulo,
    l.autor as CodAutor,
    a.nome as NomeAutor,
    l.valor as Valor,
    l.editora as CodEditora,
    e.nome as NomeEditora
from livro l
inner join autor a on l.autor = a.codautor
inner join editora e on l.editora = e.codeditora
order by l.valor desc
limit 10
