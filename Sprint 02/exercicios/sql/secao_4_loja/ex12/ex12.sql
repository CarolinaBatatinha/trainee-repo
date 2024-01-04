-- Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto 
-- em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.


-- Observação: Apenas vendas com status concluído.

with vendedor_com_menor_vendas as (
    select 
        v.cdvdd,
        v.nmvdd,
        sum(vend.qtd * vend.vrunt) as valor_total_vendas
    from
        tbvendas vend
    inner join
        tbvendedor v on v.cdvdd = vend.cdvdd
    where
        lower(vend.status) = 'concluído'
    group by
        v.cdvdd, v.nmvdd
    having
        sum(vend.qtd * vend.vrunt) > 0
)

select
    dep.cddep,
    dep.nmdep,
    dep.dtnasc,
    vcmv.valor_total_vendas
from
    tbdependente dep
inner join
    tbvendas vend on vend.cdvdd = dep.cdvdd 
inner join
    vendedor_com_menor_vendas vcmv on vcmv.cdvdd = dep.cdvdd
where
    lower(vend.status) = 'concluído'
order by vcmv.valor_total_vendas
limit 1
