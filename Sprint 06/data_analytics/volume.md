## Volume: armazenamento de dados

Uma solução para analisar dados tem que suportar enormes quantidades de dados. Portanto, precisa possuir um armazenamento que seja escalável e durável e precisa ser capaz de coletar esses dados de muitas fontes diferentes.

Os **dados relacionais** (*ou estruturados*) normalmente são armazenados em bancos de dados relacionais. Eles são estruturados por regras e constraints definidas no próprio banco de dados. Esse tipo de dados é espinha dorsal de aplicações transacionais.

Os **dados semiestruturados**, geralmente, são armazenados no banco de dados não relacional, ou também chamado de NoSQL, ou até mesmo em arquivos de JSON ou XML. Esses dados não têm uma estrutura rígida e muitas vezes, por sua própria natureza, são temporários. 

Os **dados não estruturados** possuem a forma de arquivos ou objetos, não têm uma estrutura única e representam todo o resto que uma empresa coleta e gera. Esses dados geralmente são considerados intocáveis porque não atendem às normas convencionais. Eles exigem a criação de tags e precisam ser catalogados pra serem analisados, o que impede que muitas empresas utilizem suas soluções de Data Analytics. 

Os conjuntos de dados estão cada vez maiores e mais diversificados a cada dia. Plataformas modernas de gerenciamento de dados devem capturar dados de diversas fontes em velocidade e escala. Os dados precisam ser reunidos em repositórios gerenciáveis e centrais, dividindo os silos tradicionais. Os benefícios da coleta e avaliação de todos os dados de negócios devem superar os custos.

### Introdução ao Amazon S3

As soluções de avaliação de dados podem ingerir dados de praticamente qualquer lugar. No entanto, quanto mais próximo os dados estiverem do sistema de processamento, melhor será o desempenho desse sistema. Na AWS, o Amazon Simple Storage Service (Amazon S3) é o melhor lugar para armazenar todos os seus dados semiestruturados e não estruturados.

O Amazon S3 é o armazenamento para a internet. Esse serviço foi projetado para facilitar a computação em escala web para os desenvolvedores. O Amazon S3 fornece uma interface simples de serviços da web que pode ser usada para armazenar e recuperar qualquer quantidade de dados, a qualquer momento e a partir de qualquer lugar. O serviço concede acesso a todos os desenvolvedores à mesma infraestrutura altamente escalável, confiável, segura, rápida e econômica que a Amazon utiliza para executar sua própria rede global de sites. O serviço tem como objetivo maximizar os benefícios de escala e repassar esses benefícios para os desenvolvedores.

Os benefícios do Amazon S3 são:

- Armazenamento de qualquer coisa;
- Armazenamento seguro de objetos;
- Acesso HTTP nativamente on-line;
- Escalabilidade ilimitada; 
- Durabilidade de 99,999999999%.

O Amazon S3 é um armazenamento de objetos criado para armazenar e recuperar qualquer quantidade de dados de qualquer lugar.

### Conceitos do Amazon S3

Um **objeto** é composto por um arquivo e quaisquer metadados que descrevam esse arquivo. Para armazenar um **objeto** no Amazon S3, você faz o upload do arquivo que deseja armazenar no bucket. Ao fazer o upload de um arquivo, você pode definir permissões no objeto e adicionar metadados.

**Buckets** são contêineres lógicos para objetos. Você pode ter um ou mais buckets em sua conta e controlar o acesso a cada um individualmente. Você controla quem pode criar, excluir e listar objetos no bucket. Você também pode visualizar logs de acesso do bucket e seus objetos e escolher a região geográfica onde o Amazon S3 armazenará o bucket e o respectivo conteúdo.

Depois que os objetos foram armazenados em um bucket do Amazon S3, eles recebem uma **chave de objeto**. Use isso, juntamente com o nome do bucket, para acessar o objeto. Uma **chave de objeto** é um identificador exclusivo de um objeto em um bucket. Como a combinação de um bucket, chave e ID de versão identifica exclusivamente cada objeto, você pode considerar o Amazon S3 como um mapa de dados básico entre “bucket + chave + versão” e o próprio objeto. Cada objeto no Amazon S3 pode ser endereçado exclusivamente pela combinação de endpoint de serviço web, nome de bucket, da chave e, opcionalmente, a versão.

### Soluções de avaliação de dados no Amazon S3

Há muitas vantagens em usar o Amazon S3 como plataforma de armazenamento para sua solução de avaliação de dados.

- **Desacoplamento entre o armazenamento e o processamento de dados**: com o Amazon S3, é possível armazenar de modo econômico todos os tipos de dados em seus respectivos formatos nativos. Em seguida, pode-se executar quantos servidores virtuais forem necessários usando o Amazon Elastic Compute Cloud (Amazon EC2) e usar as ferramentas analíticas da AWS para processar seus dados. Também é possível otimizar suas instâncias do EC2 para fornecer as proporções corretas de CPU, memória e largura de banda para obter melhor desempenho Desacoplar seu processamento e armazenamento oferece muitos benefícios, incluindo a capacidade de processar e analisar os mesmos dados com diversas ferramentas.

- **Arquitetura de dados centralizada**: o Amazon S3 facilita a criação de um ambiente multi-tenant em que muitos usuários podem trazer suas próprias ferramentas de análise de dados para um conjunto comum de dados. Isso melhora o custo e a governança de dados em relação às soluções tradicionais, que exigem que várias cópias de dados sejam distribuídas em múltiplas plataformas de processamento. Embora isso possa exigir uma etapa adicional para carregar seus dados na ferramenta certa, ter o Amazon S3 como seu datastore central oferecerá ainda mais benefícios em relação às opções de armazenamento tradicionais.

- **Integração com serviços AWS sem cluster e sem servidor**: combinando o Amazon S3 com outros serviços AWS para consultar e processar dados. O Amazon S3 também se integra à computação sem servidor do AWS Lambda para executar código sem provisionar ou gerenciar servidores. O Amazon Athena pode consultar o Amazon S3 diretamente usando a linguagem de consulta estruturada (SQL), sem a necessidade de entrada de dados em um banco de dados relacional. Com todos esses recursos, você paga apenas pela quantidade de dados processados ou pelo tempo de computação consumido.

- **Interfaces de programação de aplicativos (APIs) padronizadas**: as APIs REST são interfaces de programação comumente usadas para interagir com arquivos no Amazon S3. As APIs RESTful do Amazon S3 são simples, fáceis de usar e compatíveis com a maioria dos principais provedor independente de software (ISV) terceirizados, incluindo o Apache Hadoop e outros fornecedores de ferramentas analíticas líderes do mercado. Isso permite que os clientes tragam as ferramentas que já conhecem e com as quais estão mais confortáveis para ajudá-los a executar análises em dados no Amazon S3.

### Introdução a data lakes

Um ***data lake*** é um repositório centralizado que permite armazenar dados estruturados, semiestruturados e não estruturados em qualquer escala. Ele é um conceito de arquitetura que ajuda você a gerenciar vários tipos de dados de fontes diferentes, tanto estruturados como não estruturados por meio de um único conjunto de ferramenta. Um *data lake* pode utilizar buckets do Amazon S3 e podemos organizar os dados em categorias dentro dele. Não importa como os dados chegaram lá ou de que tipo eles são. Você pode armazenar dados estruturados e não estruturados de maneira eficaz em um *data lake* no Amazon S3. A AWS oferece um conjunto de ferramentas para gerenciar todo *data lake* sem tratar de cada bucket como objetos separados e não associados.

Muitas empresas acabam agrupando dados em vários locais separados de armazenamento. Chamamos isso de silos. Esses silos raramente são gerenciados e mantidos pela mesma equipe e isso pode ser problemático. As inconsistências na forma como os dados foram escritos, coletados, agregados ou filtrados, podem causar dificuldades quando comparados e combinados na fase de processamento e análise.

Quando se usa a data lakes, você pode dividir esses silos de dados e trazê-los para um único repositório central gerenciado por uma única equipe, o que irá fornecer uma única e consistente fonte da verdade. Como os dados podem ser armazenados em seu formato bruto, você não precisa convertê-los, agregá-los ou filtrá-los antes de armazenar. Em vez disso, você pode deixar todo esse pré processamento pro sistema que o processa, em vez do sistema que o armazena.

### Benefícios de um data lake na AWS

- São uma solução de armazenamento de dados econômica. Você pode armazenar de forma durável uma quantidade quase ilimitada de dados usando o Amazon S3.

- Implemente a segurança e a conformidade líderes do setor. A AWS usa rigorosos mecanismos de segurança, conformidade, privacidade e proteção de dados.

- Permite que você aproveite muitas ferramentas diferentes de coleta e ingestão de dados para ingerir dados em seu data lake. Esses serviços incluem o Amazon Kinesis para dados de streaming e dispositivos AWS Snowball para grandes volumes de dados locais.

- Ajudam você a categorizar e gerenciar seus dados de forma simples e eficiente. Use o AWS Glue para entender os dados dentro do seu data lake, prepará-los e carregá-los de forma confiável em datastores. Depois que o AWS Glue cataloga seus dados, eles são imediatamente pesquisáveis, podem ser consultados e estão disponíveis para processamento de ETL.

- Ajuda você a transformar dados em informações significativas. Utilize o poder dos serviços analíticos criados para finalidades específicas em vários casos de uso, como avaliação interativa, processamento de dados usando o Apache Spark e o Apache Hadoop, data warehousing, análise em tempo real, análise operacional, painéis e visualizações.

### Amazon EMR e data lakes

As empresas começaram a perceber o poder dos data lakes. Elas podem colocar dados em um data lake e usar os frameworks de processamento distribuído de código aberto que preferirem, como os compatíveis com o Amazon EMR. O Apache Hadoop e o Spark são compatíveis com o Amazon EMR, que tem a capacidade de ajudar as empresas a implementar soluções de processamento de dados baseadas em data lakes do Amazon S3 de modo fácil, rápido e econômico.

A preparação de dados é uma tarefa enorme. Não há respostas fáceis quando se trata de limpeza, transformação e coleta de dados para seu data lake. No entanto, há serviços que podem automatizar muitos desses processos demorados. A configuração e o gerenciamento de data lakes atualmente podem envolver muitas tarefas manuais, complicadas e demoradas. Esse trabalho inclui carregar os dados, monitorar os fluxos de dados, configurar partições para os dados e ajustar a criptografia. Você também pode precisar reorganizar dados, deduplicá-los, combinar registros vinculados e auditar dados ao longo do tempo.

O AWS Lake Formation facilita a ingestão, limpeza, catalogação, transformação e proteção dos seus dados, além de disponibilizá-los para avaliação e machine learning. O Lake Formation oferece um console central no qual você pode descobrir origens dos dados, configurar trabalhos de transformação para mover dados para um data lake do Amazon S3, remover duplicações e combinar registros, catalogar dados para acesso por ferramentas analíticas, configurar políticas de segurança e acesso a dados e auditar e controlar o acesso dos serviços analíticos e de machine learning da AWS.

O Lake Formation configura automaticamente os serviços AWS básicos para garantir a conformidade com suas políticas definidas. Se você configurou trabalhos de transformação que abrangem os serviços AWS, o Lake Formation configura os fluxos, centraliza a orquestração e permite que você monitore a execução dos trabalhos.

### Introdução aos métodos de armazenamento de dados

Um **data warehouse **é um repositório central de dados estruturados de muitas origens de dados. Esses dados são transformados, agregados e preparados para relatórios e avaliaçãos de negócios. Os dados fluem para um data warehouse de sistemas transacionais, bancos de dados relacionais e outras fontes. Essas origens de dados podem incluir dados estruturados, semiestruturados e não estruturados. Essas origens de dados são transformadas em dados estruturados antes de serem armazenadas no data warehouse.

Os dados são armazenados no data warehouse usando um esquema. Um esquema define como os dados são armazenados em tabelas, colunas e linhas. O esquema impõe restrições nos dados para garantir a integridade deles. O processo de transformação muitas vezes envolve as etapas necessárias para fazer com que os dados da fonte estejam em conformidade com o esquema. Após a primeira ingestão bem-sucedida de dados no data warehouse, o processo de ingestão e transformação dos dados pode continuar em um ritmo regular.

Analistas de negócios, cientistas de dados e tomadores de decisão acessam os dados por ferramentas de business intelligence (BI), clientes SQL e outros aplicativos de análise. As empresas usam ferramentas de relatórios, painéis e análise para extrair informações dos dados, monitorar o desempenho dos negócios e corroborar a tomada de decisões. Essas ferramentas de relatórios, painéis e análises são alimentados por data warehouses, que armazenam dados com eficiência para minimizar a E/S e entregar resultados de consultas com velocidades altíssimas a centenas e milhares de usuários simultâneos.

Um subconjunto de dados de um **data warehouse** é chamado de **data mart**. Os **data marts** se concentram em apenas um assunto ou uma área funcional. Um **data warehouse** pode conter todas as fontes relevantes para uma empresa, mas um data mart pode armazenar apenas as fontes de um único departamento. Como os data marts geralmente são uma cópia dos dados já contidos em um data warehouse, eles geralmente são rápidos e simples de implementar.

### Comparação entre data warehouses e data lakes

![Comparação entre data warehouses e data lakes](imagens/2.png)

### Apache Hadoop

O Hadoop usa uma arquitetura de processamento distribuído, no qual uma tarefa é mapeada para um cluster de servidores convencionais para processamento. Cada bloco de trabalho distribuído aos servidores do cluster pode ser executado ou re-executado em qualquer um dos servidores. Os servidores do cluster usam frequentemente o Hadoop Distributed File System (HDFS) para armazenar dados localmente para processamento. Os resultados da computação realizada pelos servidores são reduzidos a um único conjunto de saída. Um nó, designado como nó principal, controla a distribuição de tarefas e pode lidar automaticamente com falhas dos servidores.

Dentre os **benefícios** do uso do Apache Hadoop estão:

- Lida melhor com a incerteza;
- Gerencia variedade de dados;
- Tem ampla seleção de soluções;
- Visa ao volume e à velocidade.

### Implementação do Hadoop com o Amazon EMR

O Amazon EMR é o serviço AWS que implementa frameworks Hadoop. O serviço fará a ingestão dos dados de praticamente qualquer tipo de origem a praticamente qualquer velocidade! O Amazon EMR consegue implementar dois sistemas de arquivos diferentes: HDFS ou Elastic MapReduce File System (EMRFS). Um sistema de arquivos é um conjunto de regras organizacionais que controlam como os arquivos são armazenados. 

### HDFS

Para lidar rapidamente com volumes enormes de dados, o sistema de processamento exigia uma maneira de distribuir a carga de leitura e gravação de arquivos em dezenas ou até centenas de servidores de alta capacidade. O HDFS éum armazenamento distribuído que permite que os arquivos sejam lidos e gravados em clusters de servidores em paralelo. Isso reduz drasticamente a duração total de cada operação.

É útil compreender o funcionamento interno de um cluster do HDFS. Um cluster do HDFS consiste primariamente em um NameNode, que gerencia os metadados do sistema de arquivos, e DataNodes, que armazenam os dados reais.

O **Amazon EMR** é o serviço AWS que implementa frameworks Hadoop. Um processo do Amazon EMR começa ingerindo dados de uma ou mais origens de dados e armazenando esses dados em um sistema de arquivos. Se estiver usando o HDFS, o sistema de arquivos será armazenado como um volume do Elastic Block Store. Esse volume de armazenamento no EMR é efêmero, o que significa que o armazenamento é de natureza temporária. Assim que os dados forem copiados para o volume do HDFS, a transformação e a avaliação dos dados serão executadas. Em seguida, os resultados são enviados para um datastore analítico, como um data lake do Amazon S3 ou um data warehouse do Amazon Redshift.

### Amazon EMRFS

O Amazon EMR oferece uma alternativa ao HDFS: o EMR File System (EMRFS). O EMRFS pode ajudar a garantir que haja uma “fonte confiável” persistente para dados do HDFS armazenados no Amazon S3. Ao implementar o EMRFS, não é necessário copiar dados para o cluster antes de transformar e analisar os dados como no HDFS. O EMRFS pode catalogar dados em um data lake no Amazon S3. O tempo economizado eliminando a etapa de cópia pode melhorar drasticamente o desempenho do cluster.

