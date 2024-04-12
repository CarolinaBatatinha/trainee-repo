import os
import boto3
import json
import tempfile
import datetime
import requests

def lambda_handler(event, context):
    api_key = os.environ['api_key']
    aws_access_key_id = os.environ['aws_access_key_id']
    aws_secret_access_key = os.environ['aws_secret_access_key']
    aws_session_token = os.environ['aws_session_token']
    bucket = 'desafio-1-carolina' 

    movies= ['203', '103', '769', '1598', '10433', '524', '112205', '398978', '466420']  
    data_movies = []

    for movie_id in movies:
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres=80&with_cast=380&with_crew=1032&language=pt-BR&include_adult=true'
        response = requests.get(url)
        movie_data = response.json()
        orcamento = movie_data.get('budget')

        df_movie = {
            'id do filme': movie_data['id'],
            'Titulo': movie_data['title'],      
            'Data de lançamento': movie_data['release_date'],
            'Sinopse': movie_data['overview'],
            'Votos': movie_data['vote_count'],
            'Média de votos': movie_data['vote_average'],
            'ID de gênero': movie_data['genre_ids'],
            'Filme adulto': movie_data['adult'],
            'Poster': movie_data['poster_path'],
            'Orçamento': orcamento
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

    s3_file_path = f"{folder_movies}/tmdb_data_1.json"
    s3.upload_file(temp_path, bucket, s3_file_path)

    return {
        'statusCode': 200,
        'body': json.dumps('Data ingestion complete!')
    }
