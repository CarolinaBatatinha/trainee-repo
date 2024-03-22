from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from os.path import abspath

spark = SparkSession \
    .builder \
    .master('local[*]') \
    .appName('Exercício Intro') \
    .getOrCreate()

caminho_absoluto = abspath('/home/carolina/Documentos/trainee-repo/Sprint 08/exercicios/exercicios-spark-batch/tarefa4/nomes_aleatorios.txt')
df_nomes = spark.read.csv(caminho_absoluto, inferSchema=True)

paises_america_sul = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Guiana', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela']

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

escolaridade = ['Fundamental', 'Médio', 'Superior']
df_nomes = df_nomes.withColumn('Escolaridade',
                               F.when(F.rand() < 1/3, escolaridade[0])  
                               .when(F.rand() < 2/3, escolaridade[1])
                               .otherwise(escolaridade[2]))

df_nomes_com_pais = df_nomes.withColumn("Pais", 
    F.element_at(
        F.array([F.lit(p) for p in paises_america_sul]),
        (F.floor(F.rand() * F.size(F.array([F.lit(p) for p in paises_america_sul]))) + 1).cast('int')))

df_nomes = df_nomes_com_pais.withColumn('AnoNascimento', (F.rand() * (2010 - 1945) +1945).cast('int'))

# 10) 
df_nomes.createOrReplaceTempView("pessoas")


query_baby_boomers = """
    SELECT Pais, COUNT(*) AS Quantidade, 'Baby Boomers' AS Geracao
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1944 AND 1964
    GROUP BY Pais
"""

query_geracao_x = """
    SELECT Pais, COUNT(*) AS Quantidade, 'Geracao X' AS Geracao
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1965 AND 1979
    GROUP BY Pais
"""

query_millennials = """
    SELECT Pais, COUNT(*) AS Quantidade, 'Millennials' AS Geracao
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1980 AND 1994
    GROUP BY Pais
"""

query_geracao_z = """
    SELECT Pais, COUNT(*) AS Quantidade, 'Geracao Z' AS Geracao
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1995 AND 2015
    GROUP BY Pais
"""

df_resultado = spark.sql(query_baby_boomers).union(
    spark.sql(query_geracao_x)).union(
    spark.sql(query_millennials)).union(
    spark.sql(query_geracao_z))

df_resultado = df_resultado.orderBy("Pais", "Geracao", "Quantidade")

df_resultado.show(df_resultado.count(), truncate=False)
