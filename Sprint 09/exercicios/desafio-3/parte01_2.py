import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1712863913177 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": [
            "s3://desafio-1-carolina/desafio-1-carolina/Raw/Local/CSV/100_records/2024/03/28/"
        ],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1712863913177",
)

# Script generated for node Drop Fields
DropFields_node1712863967290 = DropFields.apply(
    frame=AmazonS3_node1712863913177,
    paths=[
        "array.id do filme",
        "array.Titulo",
        "array.Data de lançamento",
        "array.Sinopse",
        "array.Votos",
        "array.Média de votos",
        "array.ID de gênero",
        "array.Filme adulto",
        "array.Poster",
        "array.Orçamento",
        "array",
    ],
    transformation_ctx="DropFields_node1712863967290",
)

# Script generated for node Amazon S3
AmazonS3_node1712864011194 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1712863967290,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://desafio-1-carolina/Raw/parte3/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="AmazonS3_node1712864011194",
)

job.commit()
