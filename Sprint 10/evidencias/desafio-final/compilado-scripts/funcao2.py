import os
import requests
import boto3
import json
import tempfile
import datetime

def get_movie_details(movie_id, api_key):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    response = requests.get(url)
    movie_details = response.json()
    return movie_details

def lambda_handler(event, context):
   
    api_key = os.environ['api_key']
    aws_access_key_id = os.environ['aws_access_key_id']
    aws_secret_access_key = os.environ['aws_secret_access_key']
    aws_session_token = os.environ['aws_session_token']
    bucket = 'desafio-batatinha'


    movies_data = []


    total_pages = 1  # Start with 1
    current_page = 1

    while current_page <= total_pages:

        url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres=80&with_cast=380&with_crew=1032&language=pt-BR'


        response = requests.get(url)
        movies_response = response.json()

        if total_pages == 1:
            total_pages = movies_response['total_pages']


        for movie_data in movies_response['results']:

            movie_id = movie_data['id']
            movie_details = get_movie_details(movie_id, api_key)


            production_countries = movie_details.get('production_countries')
            release_date = movie_details.get('release_date')
            revenue = movie_details.get('revenue')
            runtime = movie_details.get('runtime')
            spoken_languages = movie_details.get('spoken_languages')
            production_companies = movie_details.get('production_companies')
            budget = movie_details.get('budget')


            movie_info = {
                'id': movie_id,
                'title': movie_data['title'],
                'vote_count': movie_data.get('vote_count'),
                'vote_average': movie_data.get('vote_average'),
                'popularity': movie_data.get('popularity'),
                'release_date': release_date,
                'budget': budget,
                'spoken_languages': spoken_languages
            }
            movies_data.append(movie_info)


        current_page += 1


    temp_dir = tempfile.mkdtemp()
    temp_path = f"{temp_dir}/tmdb_data.json"
    data_fdt = {"movies": movies_data}

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
