import boto3
import os
from datetime import datetime

data = datetime.now().strftime('%Y/%m/%d')


def upload_arquivo(arquivo, raw, local, formato, especificacao, data):
    s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id="ASIA4MTWHDZK3AWW2CED",
                    aws_secret_access_key="Z92dhqcsAB16gR9bs9xPtXpmb4QsvW1xjp2fx1IO", 
                    aws_session_token="IQoJb3JpZ2luX2VjEHMaCXVzLWVhc3QtMSJHMEUCIQDSUg8h2Wt0Lnv/oOvf3/5Ea9+Z1jU3zQHxBMoJU8A28AIgcu5Q4r735raerJwab3SZfNK5ZEqefkJkXMRn/7XKoQEqqgMIrP//////////ARAAGgw4NTE3MjUxOTY4ODUiDLDOsUa36TvHoUQ9jCr+AgE3kDKNObkskmTUJHrzHggUK3rP/LN8oJIW68ugRFGM46ZvZn8jp+9bLLXRQD8jnzWhjviIkI/PdRXec7sjcfoZaTJmxE9U2URutYvnbYRmTHIQwQJXN7AhFfTWwak9uF/63nmoE/iwHN5g5SvNvdxNPkn825+WC3nPkkl0cjUpvIRzsJxRWjlvI2g03StSHhFEfi6sDw/KSI0wQTinkausE6kTfGZGukmGvY/hnV/z60OGAGFBPPf3aAKWtnl8eOmpOxgx/cbNcT1u9QQE80AICOPz8lM2RCB8lrnloyd8pK8z1JMixsaMu4qWdKe+UAdSk9tLRHxo8XKf5iSEO7NPESt3YHzz4OddmTNs1WikY62v+iqXzOJj0wOXmRGXp0gpYg0gmxpr445X3NJl8JMxVavPunKkplA8ivPTR69VHQtTQ8BCOZiOPLTZ2XhSACdfsCtgKYatC6DYe50nk7tu9/UdDRqYS+le5XvbDw2a9bGibFxwtHRdAErWXJUw6uL1sAY6pgGKlHw/a0TveI5mB6Aq7WoiXrkEzU+ZC7K4v7hyMF1K+0PV9tqihd2vhTyv6mX20A/JvIYtr42GXWAIHPtP1AHlU0mRxDWF4S5Rxw502NlllrsiDqgQygnDnyrdHR3Pks1I6ed2fZ7haeOr3EAtDm2ngAM9kCu07TX4mCSDGfBJd3ayH4Ln0Ebyzy1r+wmoWcnX+umVNeu9VKgRlRHo0lr+0fE6JsTb")

    key = f'{raw}/{local}/{formato}/{especificacao}/{data}/{os.path.basename(arquivo)}'

    try:
        s3.upload_file(arquivo, 'desafio-batatinha', key)
        print(f'Arquivo {os.path.basename(arquivo)} enviado para o bucket com sucesso!')
    except Exception as e:
        print(f'Arquivo {os.path.basename(arquivo)} não enviado para o bucket: {e}')


def main():
    movies_path = './movies.csv'
    series_path = './series.csv'
    upload_arquivo(movies_path, 'Raw', 'Local', 'CSV', 'Movies', data)
    upload_arquivo(series_path, 'Raw', 'Local', 'CSV', 'Series', data)

if __name__ == "__main__":
    main()
