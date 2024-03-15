import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, desc

# Inicializa o contexto do Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Parâmetros
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Lê o arquivo CSV do S3
df = spark.read.csv("s3://lab-glue-carolina/lab-glue/input/nomes.csv", header=True, inferSchema=True)

# Imprime o schema
print("Schema do DataFrame:")
df.printSchema()

# Altera a caixa dos valores da coluna nome para maiúsculo
df = df.withColumn("nome", col("nome").upper())

# Imprime contagem de linhas
print("Contagem de Linhas no DataFrame:", df.count())

# Contagem de nomes por ano e sexo
contagem_nomes = df.groupBy("ano", "sexo").agg(count("*").alias("total_registros"))
contagem_nomes = contagem_nomes.orderBy("ano", ascending=True)

# Nome feminino com mais registros
mais_registros_feminino = df.filter(df.sexo == "F").groupBy("nome", "ano").agg(count("*").alias("total_registros")).orderBy(desc("total_registros")).first()

# Nome masculino com mais registros
mais_registros_masculino = df.filter(df.sexo == "M").groupBy("nome", "ano").agg(count("*").alias("total_registros")).orderBy(desc("total_registros")).first()

# Total de registros por ano
total_registros_por_ano = df.groupBy("ano").agg(count("*").alias("total_registros_por_ano")).orderBy("ano", ascending=True)

# Imprime as primeiras 10 linhas ordenadas pelo ano
print("Primeiras 10 linhas ordenadas pelo ano:")
df.orderBy("ano").show(10)

# Escreve o conteúdo do DataFrame com os valores de nome em maiúsculo no S3
df.write.partitionBy("sexo", "ano").json("s3://lab-glue-carolina/lab-glue/frequencia_registro_nomes_eua/")

# Imprime resultados adicionais
print("Nome feminino com mais registros:", mais_registros_feminino.nome, "em", mais_registros_feminino.ano, "com", mais_registros_feminino.total_registros, "registros")
print("Nome masculino com mais registros:", mais_registros_masculino.nome, "em", mais_registros_masculino.ano, "com", mais_registros_masculino.total_registros, "registros")
print("Total de registros (masculinos e femininos) para cada ano:")
total_registros_por_ano.show()

# Finaliza o job
job.commit()