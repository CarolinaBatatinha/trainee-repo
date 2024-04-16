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

df = spark.read.format("json").load("s3://desafio-batatinha/Raw/Local/TMDB/json/2024/04/15/tmdb_data.json")

df.printSchema()
df.show()

read_df = df.withColumn("explode", expr("explode_outer(filmes)"))

processed_data = read_df.select(
    col("explode.idFilme"),
    col("explode.Titulo"),
    col("explode.DataDeLancamento"),
    col("explode.Sinopse"),
    col("explode.Votos"),
    col("explode.MediaDeVotos"),
    col("explode.FilmeAdulto"),
    col("explode.Poster"),
    col("explode.Orcamento_US")
)

processed_data.write.parquet("s3://desafio-batatinha/Trusted/TMDB")
job.commit()