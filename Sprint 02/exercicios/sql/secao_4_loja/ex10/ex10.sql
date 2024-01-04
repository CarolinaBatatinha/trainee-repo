-- A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. 
-- O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados 
-- com status concluído.

-- As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem 
-- decrescente arredondado na segunda casa decimal.

select 
    tbvendedor.nmvdd as vendedor,
    round(sum(tbvendas.qtd * tbvendas.vrunt), 2) as valor_total_vendas,
    round(sum(tbvendas.qtd * tbvendas.vrunt * tbvendedor.perccomissao)/100, 2) as comissao
    
from tbvendedor
inner join tbvendas on tbvendedor.cdvdd = tbvendas.cdvdd
inner join tbestoqueproduto on tbestoqueproduto.cdpro = tbvendas.cdpro

where tbvendas.status = 'Concluído'
group by 
    tbvendedor.cdvdd, 
    tbvendedor.nmvdd, 
    tbvendedor.perccomissao
order by comissao desc
