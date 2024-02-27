WITH nomes_classificados AS (
    SELECT
        nome,
        ROW_NUMBER() OVER (PARTITION BY FLOOR(ano/10) ORDER BY total DESC) AS classificacao,
        FLOOR(ano/10) * 10 AS decada
    FROM
        meubanco.minha_tabela
    WHERE
        ano >= 1950
)
SELECT
    nome,
    decada
FROM
    nomes_classificados
WHERE
    classificacao <= 3
ORDER by decada;