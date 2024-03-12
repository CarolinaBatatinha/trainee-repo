from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("Contagem de Palavras") \
    .getOrCreate()

textFile = spark.sparkContext.textFile("README.md")

words = textFile.flatMap(lambda line: line.split())

wordCounts = words.map(lambda word: (word.lower(), 1))

result = wordCounts.reduceByKey(lambda x, y: x + y)

result.foreach(print)