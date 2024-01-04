-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas 
-- vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

select tbvendedor.cdvdd,tbvendedor.nmvdd
from tbvendedor
left join tbvendas on tbvendedor.cdvdd = tbvendas.cdvdd

where tbvendas.status = 'Concluído'
group by tbvendedor.cdvdd, tbvendedor.nmvdd
order by count(tbvendas.cdven) desc
limit 1