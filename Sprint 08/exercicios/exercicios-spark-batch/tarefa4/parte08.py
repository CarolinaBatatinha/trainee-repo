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

paises_america_sul = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela']

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

df_select = df_nomes.filter(F.col('AnoNascimento') >= 2000)

df_nomes.createOrReplaceTempView('pessoas')
df_select_sql = spark.sql('SELECT * FROM pessoas WHERE AnoNascimento >= 2000')

# 8)

millennials_count = df_nomes.filter((F.col('AnoNascimento') >= 1980) & (F.col('AnoNascimento') <= 1994)).count()

print(f'\nNúmero de pessoas da geração Millennials: {millennials_count}')
