# Sprint 7

A Sprint 7 trouxe conceitos sobre o **PySpark** e o **Apache Hadoop**, dando continuidade à trilha de aprendizado.

# PySpark

O PySpark é uma biblioteca Python para processamento de dados distribuído, construída sobre o Apache Spark. 

## DataFrames
Resumidamente, na criação de DataFrames usando PySpark, os principais conceitos e comandos incluem:

**1. SparkSession:**  
Inicia o ambiente Spark e fornece uma interface para trabalhar com DataFrames.
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("exemplo").getOrCreate()
```

**2. Leitura de dados:**  
Carrega dados de diferentes fontes, como CSV, JSON, Parquet, etc.
```python
df = spark.read.csv("caminho/do/arquivo.csv", header=True, inferSchema=True)
```

**3. Exibição de dados:**  
Mostra os primeiros registros do DataFrame.
```python
df.show()
```

**4. Esquema do DataFrame:**  
Exibe a estrutura do DataFrame.
```python
df.printSchema()
```

**5. Seleção de colunas:**  
Seleciona colunas específicas do DataFrame.
```python
df.select("coluna1", "coluna2")
```

**6. Filtragem de dados:**  
Aplica condições para filtrar linhas do DataFrame.
```python
df.filter(df["coluna"] > 50)
```

**7. Agrupamento e agregação:**  
Agrupa dados com base em uma ou mais colunas e realiza operações de agregação.
```python
df.groupBy("coluna").agg({"outra_coluna": "sum"})
```

**8. Criação de colunas:**  
Adiciona novas colunas ao DataFrame.
```python
df.withColumn("nova_coluna", df["coluna"] * 2)
```

**9. Renomeação de colunas:**  
Altera o nome de uma coluna existente.
```python
df.withColumnRenamed("coluna_antiga", "coluna_nova")
```

**10. Operações de join:**  
Combina dois DataFrames com base em uma condição.
```python
df1.join(df2, df1["chave"] == df2["chave"], "inner")
```

## Spark SQL

O Spark SQL é um módulo do Apache Spark que fornece uma interface para consultar dados estruturados usando SQL, além de suportar operações em DataFrames e Datasets. 

A consulta SQL permite executar consultas SQL diretamente em DataFrames ou visualizar tabelas temporárias registradas.
```python 
# Exemplo de execução de consulta SQL em um DataFrame
df.createOrReplaceTempView("tabela_temporaria")
resultado = spark.sql("SELECT coluna1, coluna2 FROM tabela_temporaria WHERE coluna3 > 50")
```

Um DataFrame pode ser registrado como uma **tabela temporária** para realizar consultas SQL sobre ele.
```python
df.createOrReplaceTempView("tabela_temporaria")
```

O Spark SQL também dá suporte a **consultas aninhadas**, permitindo operações complexas e agregações em dados distribuídos.
```python 
consulta_aninhada = spark.sql("SELECT AVG(coluna) FROM (SELECT * FROM tabela_temporaria WHERE coluna > 50)")
```
Ele também possibilita a **integração com o Apache Hive**, permitindo a execução de consultas em tabelas Hive usando Spark SQL.
```python
# Configuração para usar Hive no Spark SQL
spark.sql("SET spark.sql.catalogImplementation=hive")
```

Os **joins** no Spark SQL permitem combinar dados de duas ou mais tabelas com base em condições específicas. Utiliza-se a cláusula JOIN para combinar tabelas. As condições de junção são especificadas na cláusula ON.
```sql 
SELECT *
FROM tabela1
JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
```

O **Spark SQL** suporta diferentes tipos de joins, incluindo **INNER JOIN**, **LEFT JOIN**, **RIGHT JOIN** e **FULL OUTER JOIN**.

Além do uso com tabelas registradas no Spark SQL, é possível realizar joins diretamente em DataFrames usando métodos específicos.
```python
# Exemplo de INNER JOIN com DataFrames
resultado = df1.join(df2, df1["coluna"] == df2["coluna"], "inner")
```

## Importação e exportação de dados

No PySpark, a importação e exportação de dados envolvem operações de leitura e escrita em diferentes formatos. Aqui estão algumas maneiras resumidas de realizar essas operações:

**- Importação de Dados:**  
Utiliza-se o método *read* do objeto SparkSession para ler dados de várias fontes, como CSV, JSON, Parquet, etc.
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("exemplo").getOrCreate()

# Exemplo de leitura de dados CSV
df = spark.read.csv("caminho/do/arquivo.csv", header=True, inferSchema=True)
```

**- Exportação de Dados:**  
O método *write* é usado no DataFrame para exportar dados para diferentes formatos. Especificar o formato e o caminho de saída é fundamental.
```python
# Exemplo de escrita de dados no formato Parquet
df.write.parquet("caminho/do/salvamento/parquet")
```

O PySpark suporta diversos formatos, como CSV, JSON, Parquet, Avro, ORC, entre outros. Basta especificar o formato desejado durante a leitura ou escrita.
```python
# Exemplo de leitura de dados JSON
df_json = spark.read.json("caminho/do/arquivo.json")

# Exemplo de escrita de dados no formato Avro
df.write.format("avro").save("caminho/do/salvamento/avro")
```

Outro ponto importante para salientar é que, ao importar e exportar, é possível configurar várias opções, como delimitadores em CSV, compressão, modo de escrita, etc.
```python
# Exemplo de leitura de dados CSV com configurações
df_csv = spark.read.option("delimiter", ";").csv("caminho/do/arquivo.csv")

# Exemplo de escrita de dados Parquet com compressão
df.write.option("compression", "gzip").parquet("caminho/do/salvamento/parquet_comprimido")
```

Além disso, a escolha do formato e as opções de configuração dependerão do tipo de dados e dos requisitos específicos do projeto.

## Particionamento, Bucketing, Cache e Persistência no Spark

**Particionamento** é a divisão lógica dos dados em partes menores, permitindo o processamento paralelo. No Spark, pode-se definir partições ao ler ou escrever dados.
```python
# Exemplo de leitura com especificação de partições
df = spark.read.csv("caminho/do/arquivo.csv", header=True, inferSchema=True).repartition(4)
```

**Bucketing** diz respeito a uma técnica que distribui dados em um número fixo de baldes (buckets) com base em uma coluna. Facilita operações como joins eficientes em grandes conjuntos de dados.
```python
# Exemplo de escrita com bucketing
df.write.bucketBy(4, "coluna_bucket").saveAsTable("tabela_bucketed")
```

O **cache** é entendido como uma técnica de armazenamento temporário de dados em memória para acelerar o acesso subsequente. Pode ser aplicado a DataFrames ou RDDs.
```python
# Exemplo de cache em um DataFrame
df.cache()
```

Já a **persistência** permite armazenar dados em diferentes níveis de armazenamento, como memória, disco ou ambos. Pode ser útil para otimizar o desempenho e gerenciar o uso de recursos.
```python
# Exemplo de persistência em memória e disco
df.persist(storageLevel=pyspark.StorageLevel.MEMORY_AND_DISK)
```
Esses conceitos são cruciais para otimizar o desempenho e a eficiência do processamento de dados no Spark, especialmente ao lidar com grandes conjuntos de dados distribuídos. O particionamento e o bucketing auxiliam na organização eficiente dos dados, enquanto o cache e a persistência ajudam a minimizar a recomputação e melhorar o acesso rápido aos dados armazenados.

