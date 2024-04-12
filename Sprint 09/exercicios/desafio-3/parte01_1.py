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

input_path = "s3://desafio-1-carolina/Raw/Local/Movies/2024/03/18/movies.csv"
output_path = "s3://desafio-1-carolina/Raw/DadosProcessados"

df = spark.read.option("delimiter", "|").option("header", "true").csv(input_path)

processed_data = df.select(
    col("id"),
    col("tituloOriginal"),
    col("anoLancamento"),
    col("tempoMinutos"),
    col("genero"),
    col("notaMedia"),
    col("numeroVotos"),
)

processed_data.write.mode("overwrite").parquet(output_path)

job.commit()