## Velocidade: processamento de dados
Quando as empresas precisam de informações rápidas dos dados que estão coletando, mas os sistemas implantados simplesmente não conseguem atender às necessidades, há um problema de velocidade.

O **processamento de dados** significa a coleta e a manipulação de dados para produzir informações significativas. A coleta de dados é dividida em duas partes: coleta de dados e processamento de dados.

O processamento de dados é essencial para qualquer sistema de dados. O processamento de dados define os métodos usados para coletar dados e apresentá-los a mecanismos analíticos ou de armazenamento.

Há dois tipos de processamento: em lote ou batch, e o processamento em streaming. Para cada tipo de processamento existe uma arquitetura mais adequada para permitir níveis diferentes de análises. Processamento em batch significa que o processamento do conteúdo é em intervalos.

Portanto, você utiliza o processamento em batch quando há uma grande quantidade de dados para processar e precisa realizar isso em determinados intervalos. Por exemplo, em um agendamento ou quando atingisse determinado volume de dados. Esse tipo de processamento é executado em datasets como: logs de servidor, dados financeiros, relatórios de fraudes e clickstreams.

O processamento em Streaming significa processar dados em um fluxo contínuo, ou seja, o processamento de dados que são gerados continuamente em pequenos conjuntos de dados, medido em kilobytes. Você usaria o streaming quando precisasse de um feedback em tempo real ou insights contínuos. Esse tipo de processamento é executado em conjuntos de dados como: dados do sensor IoT, compras de comércio eletrônico, atividades de jogadores num jogo, clickstreams ou informações de redes sociais.

Muitas empresas usam os dois tipos de processamento: Streaming e Batch, no mesmo Dataset. O Streaming é usado para obter insights iniciais e feedback em tempo real, enquanto o Batch é usado para obter insights profundos de análises complexas, por exemplo, transações de cartão de crédito. Você já recebeu uma mensagem de texto alguns minutos depois de passar o cartão? Já, sim! Então, este é um alerta de prevenção de fraudes provenientes de dados de um streaming. É um processo de fluxo que acontece próximo do tempo real.

Agora, um outro processo que ocorre usando um mesmo conjunto de dados é quando a empresa de cartão de crédito processa dados referentes a tentativas de fraude. Ou seja, são os mesmos dados, em dois processos completamente diferentes, sendo atendidos em duas velocidades diferentes.

O processamento de dados e os desafios associados a ele podem ser definidos geralmente pela velocidade que os dados devem ser coletados e processados. O processamento em batch vem em duas formas diferentes: agendado e periódico. O processamento em batch agendado possui um volume muito grande de dados para serem processados em uma rotina regular: por hora, diariamente, semanalmente. Geralmente pega a mesma quantidade de dados a cada vez. Portanto, as cargas de trabalho, os workloads, são muito previsíveis. O processamento em batch periódico, ocorre de forma aleatória ou sob demanda. Esses workloads geralmente são executados quando uma determinada quantidade de dados é coletada. Isso pode tornar esses workloads um pouco imprevisíveis e difíceis de planejar.

O streaming também vem em duas formas: em tempo real e próximo do tempo real. Ambos os tipos envolvem dados de streaming que, como você já sabe, são processados rapidamente em pequenos lotes. A diferença vem na velocidade. O processamento em tempo real ocorre em milissegundos, enquanto o processamento próximo do tempo real ocorre em minutos. O processamento é sempre executado em um local de armazenamento.

No processamento em batch você normalmente usa uma única aplicação para coletar, processar e armazenar dados temporariamente, enquanto ele está sendo processado. A etapa final no processamento em batch é o carregamento dos dados em armazenamento de dados para ser feita a análise.

O Amazon EMR, um framework gerenciado com Hadoop, usa ferramentas como Apache Spark & Hive para executar processamento de dados complexos. Parte do processamento inclui fazer uma análise nos dados. Na análise em batch, todo o conjunto de dados é disponibilizado para as consultas analíticas, o que permite que análises altamente complexas, sejam executadas. O processamento em batch é comumente implementado nos casos em que há a necessidade de se obter insights profundos e análises avançadas. É importante ressaltar que a latência em um sistema de processamento em batch pode ser de minutos a horas, dependendo da complexidade do que está sendo executado.

No streaming de dados você usa vários serviços: um serviço para consumir o fluxo constante de dados, um serviço para processar e analisar o fluxo, outro para carregar os dados em um datastore analítico, se necessário.

A capacidade das soluções para processar dados depende muito dos seus requisitos. Escolher o sistema certo é essencial para uma implementação bem sucedida. Entender seus requisitos de tamanho e velocidade do batch ajudará você a selecionar os serviços adequados para sua solução deData Analytics. 

### Características da velocidade de processamento de dados

A capacidade de um sistema processar dados dependerá muito dos requisitos exigidos dele. Escolher o sistema certo é essencial para uma implementação bem-sucedida. 

**Coleta de dados**:  
  
  - **Em batch**: a velocidade é muito previsível no processamento em batch. Isso equivale a altos picos de transferência de dados em intervalos programados.

  - **Periódico**: a velocidade é menos previsível no processamento periódico. A perda de eventos programados pode sobrecarregar os sistemas e deve ser considerada.

  - **Quase em tempo real**: a velocidade é uma grande preocupação no processamento quase em tempo real. Esses sistemas exigem que os dados sejam processados em minutos após a coleta inicial dos dados. Isso pode sobrecarregar bastante os sistemas de processamento e análise envolvidos.

  - **Em tempo real**: a velocidade é a maior preocupação para sistemas de processamento em tempo real. As informações não podem levar minutos para serem processadas. Elas devem ser processadas em segundos para serem válidas e manterem sua utilidade.
  
**Processamento de dados**:

- **Batch e periódico**: após a coleta dos dados, o processamento pode ser feito em um ambiente controlado. Existe tempo para planejar os recursos apropriados.

- **Quase em tempo real e em tempo real**: a coleta de dados leva a uma necessidade imediata de processamento. Dependendo da complexidade do processamento (limpeza, depuração, curadoria), pode haver redução significativa da velocidade da solução. Planeje adequadamente.

### Aceleração de dados

Outra característica principal da velocidade dos dados é a aceleração de dados, o que significa a taxa na qual grandes coleções de dados podem ser ingeridas, processadas e analisadas. A aceleração de dados não é constante, ela vem em picos. Considere o Twitter como exemplo. Hashtags podem se tornar imensamente populares e aparecer centenas de vezes em apenas segundos, ou diminuir a velocidade para uma tag por hora. Isso é a aceleração de dados em ação. Seu sistema deve conseguir lidar de forma eficiente com o pico de centenas de tags por segundo e com a baixa demanda de uma tag por hora. 

## Atributos do processamento em batch e em stream

![Atributos do processamento em batch e em stream](imagens/3.png)

## Introdução ao processamento de dados em batch

O processamento em batch é a execução de uma série de programas ou trabalhos em um ou mais computadores sem intervenção manual. Os dados são coletados em batches de maneira assíncrona. O batch é enviado a um sistema de processamento quando condições específicas são atendidas, como um horário específico do dia. Os resultados do trabalho de processamento são enviados a um local de armazenamento que pode ser consultado posteriormente, conforme necessário.

### Processamento de dados em batch com o Amazon EMR e o Apache Hadoop

As organizações que precisam de soluções de big data estão trabalhando com dados em volume e velocidade tão altos que os ambientes tradicionais não conseguem atender às suas necessidades.

O Amazon EMR é um serviço gerenciado para a implantação de cargas de trabalho do Apache Hadoop. Além de executar o framework Apache Hadoop, você também pode executar outros frameworks distribuídos conhecidos, como Apache Spark, HBase, Presto e Flink no EMR. Você tem a vantagem adicional de poder interagir com dados em outros datastores da AWS, como o Amazon S3 e o Amazon DynamoDB. 

Os Amazon EMR notebooks oferecem um ambiente de desenvolvimento e colaboração sem servidor para consultas únicas e avaliaçãos exploratórias. Você pode manipular os dados e gerar gráficos de dados usando ferramentas gráficas avançadas. Os Amazon EMR notebooks monitoram seus trabalhos e até ajudam você a depurar o código dos notebooks.

### Exploração do Apache Hadoop

O Apache Hadoop é um sistema escalável de armazenamento e processamento de dados em batch. Ele usa hardware de servidor de commodity e fornece tolerância a falhas por meio de software. O Hadoop complementa os sistemas de dados existentes ao ingerir e processar simultaneamente grandes volumes de dados, estruturados ou não, de qualquer quantidade de fontes, o que permite uma avaliação mais profunda do que qualquer outro sistema pode oferecer. Esses resultados podem ser entregues a qualquer sistema empresarial existente para uso adicional, independentemente do Hadoop.

## Introdução ao processamento de dados de stream

O processamento de dados em stream oferece às empresas a capacidade de obter informações de seus dados em segundos após a coleta dos dados. As empresas não podem mais se dar ao luxo de ignorar ou evitar grandes quantidades de dados que estão sendo enviados por meio de aplicativos web, compras de comércio eletrônico, atividades de jogadores em jogos virtuais e informações de redes sociais.

### Processamento de big data em stream

Há vários motivos para usar soluções de dados de streaming. Em um sistema de processamento em batch, o processamento é sempre assíncrono e o sistema de coleta e de processamento costumam ser agrupados. Com soluções de streaming, o sistema de coleta (produtor) e o sistema de processamento (consumidor) são sempre separados. Os dados de streaming usam o que chamamos de produtores de dados. Cada um desses produtores pode gravar seus dados no mesmo endpoint, permitindo que vários streams de dados sejam combinados em um único stream para processamento. Outra grande vantagem é a capacidade de preservar a ordem dos dados do cliente e a capacidade de executar o consumo paralelo de dados. Isso permite que múltiplos usuários trabalhem simultaneamente nos mesmos dados.
