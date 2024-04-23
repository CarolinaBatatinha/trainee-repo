import os
import json
import requests
import pandas as pd
import boto3
import tempfile  # Adicionando import para tempfile
from datetime import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3', aws_access_key_id=os.environ["aws_access_key_id"],
                           aws_secret_access_key=os.environ['aws_secret_access_key'],
                           aws_session_token=os.environ['aws_session_token'])
        
    api_key = os.environ['api_key']
        
    lista_filmes = []
    
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres=80&with_cast=380&with_crew=1032&language=pt-BR&include_adult=true"
    response = requests.get(url)
    movie_data = response.json()
    
    for resultado in movie_data['results']: 
    
        orcamento = movie_data.get('budget')
        filme = {
                'idFilme': resultado['id'], 
                'Titulo': resultado['title'],  
                'DataDeLancamento': resultado['release_date'], 
                'Sinopse': resultado['overview'],  
                'Votos': resultado['vote_count'],  
                'MediaDeVotos': resultado['vote_average'], 
                'FilmeAdulto': resultado['adult'],  
                'Poster': resultado['poster_path'],  
                'Orcamento_US': orcamento  
            }
        lista_filmes.append(filme)
    
    temp_dir = tempfile.mkdtemp()
    temp_path = f"{temp_dir}/batch.json"
    data_fdt = {"filmes": lista_filmes}
        
    with open(temp_path, "w", encoding='utf-8') as json_file:
        encode_data = json.dumps(data_fdt, ensure_ascii=False)
        json_file.write(encode_data)
        
    s3 = boto3.client('s3', region_name='us-east-1')
    
    ymd = datetime.now().strftime('%Y/%m/%d')  # Definindo a variável 'ymd'
    chave = f'Raw/Local/TMDB/json/{ymd}/tmdb_data.json'
    
    try:
        with open(temp_path, 'rb') as file:
            s3.put_object(Body=file, Bucket='desafio-batatinha', Key=chave)
            print(f'Dados adicionais enviados para o bucket com sucesso!')
    except Exception as e:
        print(f'Houve um erro ao enviar os dados adicionais para o bucket: {e}')
    
    return {
        'statusCode': 200,
        'body': f"Os dados foram enviados com sucesso!"
    }
