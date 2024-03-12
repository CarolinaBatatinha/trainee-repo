// Carregar o conteúdo do arquivo README.md
val textFile = sc.textFile("https://github.com/CarolinaBatatinha/trainee-repo/blob/main/README.md")

// Dividir as linhas em palavras e contar a ocorrência de cada palavra
val wordCounts = textFile.flatMap(line => line.split(" ")).map(word => (word, 1)).reduceByKey(_ + _)

// Exibir o resultado
wordCounts.collect().foreach(println)
