import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col
from pyspark.sql.functions import expr

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df = spark.read.format("json").load("s3://desafio-1-carolina/desafio-1-carolina/Raw/Local/CSV/100_records/2024/03/28/tmdb_data_1.json")

df.printSchema()
df.show()

read_df = df.withColumn("explode", expr("explode_outer(filmes)"))

processed_data = read_df.select(
    col("id"),
    col("Titulo"),
    col("Data de Lançamento"),
    col("Sinopse"),
    col("Votos"),
    col("Média de votos"),
    col("ID de gênero"),
    col("Filme adulto"),
    col("Poster"),
    col("Orçamento")
)

processed_data.write.parquet("s3://desafio-1-carolina/Raw/DadosProcessados/TrustedTMDB/processed")
job.commit()