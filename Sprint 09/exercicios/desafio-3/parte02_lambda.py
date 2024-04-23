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
    # Access keys
    api_key = os.environ['api_key']
    aws_access_key_id = os.environ['aws_access_key_id']
    aws_secret_access_key = os.environ['aws_secret_access_key']
    aws_session_token = os.environ['aws_session_token']
    bucket = 'desafio-batatinha'


    movies_data = []

    # Number of pages to retrieve
    total_pages = 1  # Start with 1
    current_page = 1

    while current_page <= total_pages:
        # URL to search for movies containing the search query
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres=80&with_cast=380&with_crew=1032&language=pt-BR'

        # Request to TMDb API
        response = requests.get(url)
        movies_response = response.json()

        if total_pages == 1:
            total_pages = movies_response['total_pages']

        # Extracting relevant data from response
        for movie_data in movies_response['results']:
            # Get detailed information for each movie
            movie_id = movie_data['id']
            movie_details = get_movie_details(movie_id, api_key)

            # Extract additional details
            production_countries = movie_details.get('production_countries')
            release_date = movie_details.get('release_date')
            revenue = movie_details.get('revenue')
            runtime = movie_details.get('runtime')
            spoken_languages = movie_details.get('spoken_languages')
            production_companies = movie_details.get('production_companies')
            budget = movie_details.get('budget')

            # Create dictionary with all data
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

        # Move to the next page
        current_page += 1

    # Creating JSON file
    temp_dir = tempfile.mkdtemp()
    temp_path = f"{temp_dir}/tmdb_data.json"
    data_fdt = {"movies": movies_data}

    with open(temp_path, "w", encoding='utf-8') as json_file:
        encode_data = json.dumps(data_fdt, ensure_ascii=False)
        json_file.write(encode_data)

    # S3 client setup
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
        region_name='us-east-1'
    )

    # Current Date and Formatted Date
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime('%Y/%m/%d')
    folder_movies = f'Raw/TMDB/JSON/{formatted_date}'

    # Uploading JSON file to S3
    s3_file_path = f"{folder_movies}/tmdb_data.json"
    s3.upload_file(temp_path, bucket, s3_file_path)

    return {
        'statusCode': 200,
        'body': json.dumps('Ingestao de dados completa!')
    }