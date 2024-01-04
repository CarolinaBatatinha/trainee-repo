-- Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 
-- até 2018-02-02, e que estas vendas estejam com o status concluída. 
-- As colunas presentes no resultado devem ser cdpro e nmpro.

select tbestoqueproduto.cdpro, tbvendas.nmpro
from tbestoqueproduto
join tbvendas on tbvendas.cdpro = tbestoqueproduto.cdpro

where
    tbvendas.status = 'Concluído'
    and tbvendas.dtven between '2014-02-03' and '2018-02-02'
group by tbestoqueproduto.cdpro, tbvendas.nmpro
order by sum(tbvendas.qtd) desc
limit 1