import boto3
from datetime import datetime

s3 = boto3.client('s3', 
aws_access_key_id='ASIA4MTWHDZKY3MLDPEX', 
aws_secret_access_key='yR0MT7LjGfm1qnznezgjcSRzHdQzRG5zdH/70s2L',
aws_session_token='IQoJb3JpZ2luX2VjENT//////////wEaCXVzLWVhc3QtMSJHMEUCIQCAur01M2Rd9WbC5wRuezbOB/3Kgxae86U61Ql89jlPggIgT8wsnL3Gkvlt3KPQXgSWPtMlNgNYxL7HlOzjgJ0w7eQqqgMI3f//////////ARAAGgw4NTE3MjUxOTY4ODUiDDwTs8Ow3hqRXI3Zfyr+AoXt+eoBhx3cA998W+ImomKUi1MePA7Pd1iirMmnFkkZXz1rLIsg9xlzYNGRVeX5/4Dg3mVtbvE/OnHz5djVS9w8ZZCkYGx/l1Dnyd3bem6nyfIPSZsPsnPlv/LTo9PDNqhUMfWi4DpFb2D1uRQHl0x8PuJM2l1gESsHF+omYMnjh3bujfhri5FcWOXLQJT+mI0TGM+p6s7OotBgsn9x57LxkY8a5uuYhICrJ0nlI6958aNnj51ie5m6sXJxVjyagJmssUvOxkDazf20OhWndpxALEBOhCGRbPodvijuzDavCnVObmpJgdR8iN+kM+BxlXQqRkmbYtGjpRgSpJMUDGFv5YVUCyZvmalNa8JPx8+6hiSLpcA+yiL8dKnJoHeqTNrymKw+tBCDoMfNMNaWzwAMRdXwfSrVizUaPLNNMTvAhtkZFE4V4/DjnFRLjgEh76NURwy+o+XssGkNJMnPC2DjGT7yVNH007ucoRlKEGU//2BvMd12ACQpo50MGf8w+qzirwY6pgE7w0Dgj8XdY8YBAoK6UtYDo19VsrPn+fTHov1Vx4KziTJXnwujyjvHj7ZXNC6v4woQnv4pz3Sx+bizE/uA+FVRbefo2yZNwFe/fgAThYFBq1wJhqrG1xfYtBaoGFcbWhSw6JIlEkF7qKov+w5Uc8iOkCtwI5DYO/nb41PioOAqtf2eCWGq+cRu7k1Bl1ufUnZWvp+zs4Ea6Q9FEX09wgUMex6FVNhl')

bucket_name = 'desafio-1-carolina'
storage_layer = 'Raw'
data_origin = 'Local'
data_format = 'CSV'
processing_date = datetime.now().strftime('%Y/%m/%d')

s3.upload_file('/app/movies.csv', 'desafio-1-carolina','Raw/Local/Movies/2024/03/18/movies.csv')

s3.upload_file('/app/series.csv', 'desafio-1-carolina','Raw/Local/Series/2024/03/18/series.csv')

print("Dados carregados com sucesso para o S3 no bucket desafio-1-carolina!")
