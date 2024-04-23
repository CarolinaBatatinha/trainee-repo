import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
job_name = args['JOB_NAME']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(job_name, args)

schema = (
    col('idFilme'),
    col('titulo'),
    col('lancamento'),
    col('contagemVotos'),
    col('mediaVotos'),
    col('popularidade'),
    col('orcamento'),
)

# Ler o arquivo Parquet
input_path = "s3://desafio-batatinha/Trusted/TMDB/"
df = spark.read.parquet(input_path)

# Selecionar apenas as colunas desejadas
selected_columns = ['titulo', 'lancamento', 'contagemVotos', 'mediaVotos', 'popularity', 'orcamento']
df_selected = df.select(*selected_columns)

# Escrever o resultado em um novo arquivo Parquet
output_path = "s3://desafio-batatinha/Refined/TMDB"
df_selected.write.parquet(output_path)

job.commit()
