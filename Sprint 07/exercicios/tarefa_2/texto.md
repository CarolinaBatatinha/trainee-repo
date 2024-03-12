- É realizado o pull da imagem 'jupyter/all-spark-notebook'
```bash
docker pull jupyter/all-spark-notebook
```
- Cria-se um container a partir dessa imagem
```bash
docker run -it -p 8888:8888 jupyter/all-spark-notebook
```

- Clica na URL de acesso ao Jupyter Lab

- Descobre o id do container com o comando Docker
```bash
docker ps
```

- Em outro terminal, executa o pypsark no container, acrescentando o id do container
```bash
docker exec -it ca1a53c067ca pyspark  
```

- No terminal interativo do Spark, se executa os comandos Spark necessários para contar a quantidade de ocorrências de cada palavra no arquivo README.md.

docker cp /home/carolina/Documentos/trainee-repo/README.md naughty_shaw:/home/jovyan/README.md
