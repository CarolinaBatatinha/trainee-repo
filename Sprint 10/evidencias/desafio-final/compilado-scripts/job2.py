import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, explode


args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


df = spark.read.option("multiline", "true").json("s3://desafio-batatinha/Raw/TMDB/JSON/2024/04/22/tmdb_data.json")


exploded_df = df.select(explode("movies").alias("explode"))


processed_data = exploded_df.select(
    col("explode.id").alias("idFilme"),
    col("explode.title").alias("titulo"),
    col("explode.release_date").alias("lancamento"),
    col("explode.vote_count").alias("contagemVotos"),
    col("explode.vote_average").alias("mediaVotos"),
    col("explode.popularity"),
    col("explode.budget").alias("orcamento")
)


processed_data.write.parquet("s3://desafio-batatinha/Trusted/TMDB")
job.commit()
