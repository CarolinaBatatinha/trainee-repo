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

# 3) 
df_nomes = df_nomes.withColumn('Escolaridade',
                               F.when(F.rand() < 1/3, 'Fundamental')
                               .when(F.rand() < 2/3, 'Médio')
                               .otherwise('Superior'))

df_nomes.show(10)
