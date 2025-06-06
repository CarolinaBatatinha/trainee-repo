from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from os.path import abspath

#1)
spark = SparkSession\
    .builder\
    .master('local[*]')\
    .appName('Exercicio Intro')\
    .getOrCreate()

caminho_absoluto = abspath('/home/carolina/Documentos/trainee-repo/Sprint 08/exercicios/exercicios-spark-batch/tarefa4/nomes_aleatorios.txt')
df_nomes = spark.read.csv(caminho_absoluto, inferSchema = True)

df_nomes.show(5)
