import os
import json
import requests
import pandas as pd
import boto3
from datetime import datetime

# Configurações

api_key = os.environ['api_key']
BUCKET_NAME = "desafio-1-carolina"
STORAGE_LAYER = "Raw"
DATA_ORIGIN = "Local"
DATA_FORMAT = "CSV"
SPECIFICATION = "100_records"
AWS_REGION = "us-east-1"
AWS_ACCESS_KEY_ID = os.environ['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = os.environ['aws_secret_access_key']
AWS_SESSION_TOKEN= os.environ['aws_session_token']

s3_client = boto3.client(
    's3',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN
)

def lambda_handler(event, context):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres=80&with_cast=380&with_crew=1032&language=pt-BR&include_adult=true"
    response = requests.get(url)
    data = response.json()

    filmes = []

    for movie in sorted(data['results'], key=lambda x: x['release_date']):
        orcamento = movie.get('budget')
        df = {
            'id do filme': movie['id'],
            'Titulo': movie['title'],      
            'Data de lançamento': movie['release_date'],
            'Sinopse': movie['overview'],
            'Votos': movie['vote_count'],
            'Média de votos': movie['vote_average'],
            'ID de gênero': movie['genre_ids'],
            'Filme adulto': movie['adult'],
            'Poster': movie['poster_path'],
            'Orçamento': orcamento
        }
        filmes.append(df)

    df = pd.DataFrame(filmes)

    # Função para gravar no S3
    def write_to_s3(data, filename):
        bucket_path = f"{BUCKET_NAME}/{STORAGE_LAYER}/{DATA_ORIGIN}/{DATA_FORMAT}/{SPECIFICATION}"
        current_date = datetime.now().strftime('%Y/%m/%d')
        s3_key = f"{bucket_path}/{current_date}/{filename}"

        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=s3_key,
            Body=json.dumps(data)
        )

    # Quebrar os dados em lotes de 100 registros e gravar no Amazon S3
    chunks = [filmes[i:i + 100] for i in range(0, len(filmes), 100)]
    for i, chunk in enumerate(chunks):
        filename = f"tmdb_data_{i+1}.json"
        write_to_s3(chunk, filename)

    return {
        'statusCode': 200,
        'body': 'Os dados do TMDB foram salvos no S3 com sucesso!'
    }
