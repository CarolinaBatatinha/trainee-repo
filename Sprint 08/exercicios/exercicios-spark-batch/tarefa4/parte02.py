from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from os.path import abspath

spark = SparkSession\
    .builder\
    .master('local[*]')\
    .appName('Exercício Intro')\
    .getOrCreate()

caminho_absoluto = abspath('/home/carolina/Documentos/trainee-repo/Sprint 08/exercicios/exercicios-spark-batch/tarefa4/nomes_aleatorios.txt')
df_nomes = spark.read.csv(caminho_absoluto, inferSchema = True)

# 2)
df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')
df_nomes.show(10)