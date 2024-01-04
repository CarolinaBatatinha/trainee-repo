-- Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter 
-- apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa
-- a quantidade de livros em ordem decrescente.

select count(*) as quantidade, editora.nome, endereco.estado, endereco.cidade
from editora 
inner join endereco on endereco.codendereco = editora.endereco
inner join livro on livro.editora = editora.codeditora 

group by editora.nome
order by quantidade desc 
limit 5

