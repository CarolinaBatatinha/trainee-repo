-- Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. 
-- Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

-- Observação: Apenas vendas com status concluído.

select
    vend.estado,
    round(avg(vend.qtd * vend.vrunt), 2) as gastomedio
from tbvendas vend
-- INNER JOIN
--     tbcliente c ON v.id_cliente = c.id_cliente
where vend.status = 'Concluído'
group by vend.estado
order by gastomedio DESC;
