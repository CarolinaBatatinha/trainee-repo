import os
import boto3
import json
import tempfile
import datetime
import urllib.request

def lambda_handler(event, context):
    api_key = os.environ['api_key']
    aws_access_key_id = os.environ['aws_access_key_id']
    aws_secret_access_key = os.environ['aws_secret_access_key']
    aws_session_token = os.environ['aws_session_token']
    bucket = 'desafio-batatinha'

    movies = []
    data_movies = []

    for movie_id in movies:
        # Obtendo detalhes básicos do filme
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR'
        response = urllib.request.urlopen(url)
        movie_details = json.loads(response.read().decode('utf-8'))
        
        # Obtendo detalhes adicionais do filme
        movie_data_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
        movie_data_response = urllib.request.urlopen(movie_data_url)
        movie_data = json.loads(movie_data_response.read().decode('utf-8'))

        df_movie = {
            'idFilme': movie_details['id'],
            'titulo': movie_details['title'],
            'lancamento': movie_data.get('release_date'),
            'sinopse': movie_details['overview'],
            'contagemVotos': movie_details.get('vote_count'),
            'mediaVotos': movie_details.get('vote_average'),
            'popularidade': movie_details.get('popularity'),
            'orcamento': movie_details.get('budget')
        }
        data_movies.append(df_movie)

    temp_dir = tempfile.mkdtemp()
    temp_path = f"{temp_dir}/data.json"
    data_fdt = {"filmes": data_movies}

    with open(temp_path, "w", encoding='utf-8') as json_file:
        encode_data = json.dumps(data_fdt, ensure_ascii=False)
        json_file.write(encode_data)

    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
        region_name='us-east-1'
    )

    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime('%Y/%m/%d')
    folder_movies = f'Raw/TMDB/JSON/{formatted_date}'

    s3_file_path = f"{folder_movies}/tmdb_data.json"
    s3.upload_file(temp_path, bucket, s3_file_path)

    return {
        'statusCode': 200,
        'body': json.dumps('Ingestao de dados completa!')
    }
