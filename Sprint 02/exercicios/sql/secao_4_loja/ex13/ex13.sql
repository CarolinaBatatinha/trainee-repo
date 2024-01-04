-- Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  
-- As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

select
    p.cdpro,
    vend.nmcanalvendas,
    vend.nmpro,
    sum(vend.qtd) as quantidade_vendas
from tbvendas vend
inner join tbestoqueproduto p on vend.cdpro = p.cdpro

where 
    vend.status = 'Concluído'
    and (vend.nmcanalvendas = 'Ecommerce' or vend.nmcanalvendas = 'Matriz')
group by p.cdpro, vend.nmcanalvendas, vend.nmpro
order by quantidade_vendas asc
limit 10;
