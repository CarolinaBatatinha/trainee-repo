# from pyspark.sql import SparkSession
# from pyspark.sql import functions as f
# from os.path import abspath

# spark = SparkSession\
#     .builder\
#     .master('local[*]')\
#     .appName('Exercício Intro')\
#     .getOrCreate()

# caminho_absoluto = abspath('nomes_aleatorios.txt')
# df_nomes = spark.read.csv(caminho_absoluto, inferSchema = True)

# # 3)

# escolaridade = ['Fundamental', 'Médio', 'Superior']

# df_nomes = df_nomes.withColumn('Escolaridade',
#                             f.when(f.rand() < 1/3, escolaridade[0])
#                             .when(f.rand() < 2/3, escolaridade[1])
#                             .otherwise(escolaridade[2]))

# df_nomes.show(10)

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from os.path import abspath

spark = SparkSession \
    .builder \
    .master('local[*]') \
    .appName('Exercício Intro') \
    .getOrCreate()

caminho_absoluto = abspath('nomes_aleatorios.txt')
df_nomes = spark.read.csv(caminho_absoluto, inferSchema=True)

# Adicionando uma nova coluna 'Escolaridade' com valores aleatórios
df_nomes = df_nomes.withColumn('Escolaridade',
                               F.when(F.rand() < 1/3, 'Fundamental')
                               .when(F.rand() < 2/3, 'Médio')
                               .otherwise('Superior'))

# Exibindo os 10 primeiros registros
df_nomes.show(10)
