-- Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO 
-- situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. 
-- Não podem haver nomes repetidos em seu retorno.

select distinct autor.nome
from autor
inner join livro on livro.autor = autor.codautor
inner join editora on editora.codeditora = livro.editora 
inner join endereco on endereco.codendereco = editora.endereco

where endereco.estado not in ('RIO GRANDE DO SUL', 'PARANÁ', 'SANTA CATARINA')
order by autor.nome asc

