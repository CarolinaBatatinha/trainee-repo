Para realizar as atividades propostas, você pode seguir os seguintes passos:

1. Criar nova camada (layer) no AWS Lambda para as libs necessárias à ingestão de dados:

    - Acesse o console da AWS e navegue até o serviço Lambda.

    - Na guia "Camadas", clique em "Criar camada".

    - Escolha "Carregar um arquivo .zip" e faça upload de um arquivo .zip contendo as bibliotecas necessárias para a ingestão de dados, como por exemplo, requests e boto3.

    - Defina um nome e uma descrição para a camada e clique em "Criar".

2. Implementar o código Python em AWS Lambda para consumo de dados do TMDB:

    - Crie uma nova função Lambda e configure-a para usar a camada criada anteriormente.

    - Escreva o código Python para consumir os dados do TMDB utilizando a biblioteca requests.

    - Utilize a biblioteca boto3 para gravar os dados no AWS S3, seguindo o padrão de path especificado.

    - Teste a função Lambda para garantir que está funcionando corretamente.

    - Configure um gatilho para acionar a função Lambda periodicamente, utilizando o CloudWatch Event ou Amazon EventBridge, para realizar extrações periódicas de dados do TMDB.

Certifique-se de seguir as práticas recomendadas de segurança, como o gerenciamento de permissões IAM para acessar recursos da AWS e a proteção de informações sensíveis, como chaves de API. Além disso, faça testes adequados para garantir que sua função Lambda esteja funcionando corretamente antes de implantá-la em produção.