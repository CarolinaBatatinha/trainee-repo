Meu nome é Carolina e faço parte da turma de dezembro de 23 do Programa de Bolsas AWS Cloud Data Engineering da Compass UOL.

- [x] *Qual foi o gênero de filmes e séries abordado e qual foi o refinamento que você definiu para sua entrega final?*

Por fazer parte da Squad 2, escolhi analisar os dados de filmes do gênero Crime, buscando observar os filmes do gênero em questão, estrelados por Robert De Niro e dirigidos por Martin Scorsese.

- [x] *Quais foram as etapas do desafio? Como você as desenvolveu? Houveram dificuldades? Nos mostre um pouco do código em execução*

O desafio proposto durante o programa de bolsas foi dividido em 4 etapas.

Inicialmente foi realizado o carregamento dos arquivos .csv disponibilizados no início da tarefa utilizando técnicas de ETL. Foi criado um script em Python a ser usado no AWS Glue (job1) que criou a pasta Raw e suas subpastas que acomodaram um arquivo .csv.

Em seguida, compreendeu a captura de dados existentes na API do TMBD, sendo que as informações coletadas foram persistidas dentro do AWS S3. Para tanto, criei uma função (funcaoII) no AWS Lambda, que extraiu dados relevantes da API, além da elaboração de um dicionário com todos dados selecionados.

O processamento dos dados da camada Trusted persistiu todas as informações no formato parquet através da execução dois jobs (job2 e job3). No job2, criei e usei um script na AWS Glue que leu o arquivo .csv da pasta Raw e criou um outro arquivo na pasta Trusted no formato .json. Ao executar a funcaoIII, obtive detalhes adicionais para o refinamento das informações. O job3 tratou de refinar os dados localizados na pasta Trusted, através da seleção das colunas desejadas do arquivo parquet no AWS S3. Nesse processo, um novo arquivo parquet foi lançado na pasta recém-criada e entitulada Refined.

Durante o desafio, também foi construído um banco de dados (refined_db) que hospeda as tabelas entituladas csv e tmdb (ambas localizadas na pasta Trusted). A modelagem dos dados refinados pode ser vista em Data Catalog/ Tables. Esse passo é importante para que os dados estejam disponíveis para o QuickSight, que é uma ferramenta de visualização, além da composição do dashboard, que trouxe os insights extraídos. 

Não se pode deixar de falar também do uso do componente crawler no AWS Glue, que funcionou como um explorador da estrutura dos dados armazenados em diversas fontes, automatizando o processo de descoberta e catalogação de metadados sobre os dados.

Por fim, um dashboard foi criado no AWS QuickSight buscando atender o consumo e a apresentação dos dados coletados ao longo do desafio. O refinamento escolhido por mim, como dito anteriormente, envolve a análise de filmes do gênero crime, estrelados por Robert De Niro e dirigidos por Martin Scorsese.

- [x] *Como ficou seu modelo de dados? Apresente via diagrama ou utilizando o Glue Catalog. Importante descrever como você imaginou seu modelo dimensional.*

O Modelo de dados pode ser consultado através do Data Catalog dentro do AWS Glue. A importância desse evento se dá pela definição da natureza dos dados para que a análise atendesse os requisitos propostos pela tarefa.

- [x] *Como ficou seu dashboard? O que os dados estão nos contando? Mostre os dashboards funcionando de forma responsiva.*

Antes de mais nada, é preciso relembrar que a sintonia entre Robert De Niro e Martin Scorsese é um ponto indiscutível na história do cinema mundial, marcada por sua longevidade e pelo impacto na indústria cinematográfica. Essa parceria se iniciou em 1973, com "Caminhos Perigosos", e desde então essa parceria tem sido responsável por uma série de obras-primas que eternizam a essência da experiência humana com grande intensidade e profundidade emocional. 

Para conduzir essa análise, escolhi os seguintes dados: título, avaliação média do filme, contagem dos votos, data de lançamento, orçamento e popularidade dentro da plataforma. Ainda criei um novo campo calculado entitulado "TOTAL DE FILMES" para que se criasse um widget capaz de, com o uso de consulta SQL, contar a quantidade de filmes que atendiam aos requisitos da minha análise. Além desse campo criado, relacionei a avaliação média dos filmes e a contagem dos votos através de um gráfico de dispersão, mostrando a quantidade de pessoas que contribuíram com suas opiniões sobre determinado filme. Também foi notada a relação entre o orçamento e sua popularidade através de outro gráfico de dispersão, permitindo compreender a eficiência do investimento, já que, se um filme alcança alta popularidade com um orçamento relativamente baixo, isso sugere que produção foi bem sucedida em atrair o público, bem como sua rentabilidade.

- [x] *Como você imagina que os conhecimentos obtidos no decorrer do Programa de Bolsas podem gerar valor para os clientes da Compass?*

Dessa maneira, os conhecimentos adquiridos durante o Programa de Bolsas têm o potencial de gerar valor significativo para os clientes de diversas formas. Uma delas é a eficiência na análise de dados, permitindo carregar, transformar e persistir dados de diferentes fontes em um formato estruturado e acessível, possibilitando uma análise mais eficiente e abrangente. Outra forma é através da integração com APIs e a captura de dados relevantes dessa fonte, ampliando o escopo da análise com o fornecimento de informações adicionais. Também se nota a identificação de oportunidade de tendências, pois, ao analisar dados, é possível identificar de oportunidades de investimento, estratégias de marketing mais eficazes e insights sobre as preferências do público.

Em resumo, os conhecimentos adquiridos durante o Programa de Bolsas capacitam os clientes a realizar análises mais profundas, abrangentes e eficazes, proporcionando insights valiosos que podem informar suas decisões e estratégias de negócios.