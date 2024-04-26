import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_path = "s3://desafio-batatinha/Raw/Local/CSV/Movies/2024/04/15/movies.csv"
output_path = "s3://desafio-batatinha/Trusted/CSV/"

df = spark.read.option("delimiter", "|").option("header", "true").csv(input_path)

processed_data = df.select(
    col("id"),
    col("tituloOriginal"),
    col("anoLancamento"),
    col("tempoMinutos"),
    col("genero"),
    col("notaMedia"),
    col("numeroVotos"),
    col("generoArtista"),
    col("personagem")
)

processed_data.write.mode("overwrite").parquet(output_path)

job.commit()
