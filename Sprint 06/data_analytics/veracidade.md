## Veracidade: limpeza e transformação

### Tipos de origem de dados

* **Dados estruturados**:  
  Dados estruturados são armazenados em um formato tabular, muitas vezes em um sistema de gerenciamento de banco de dados (DBMS). Esses dados são organizados com base em um modelo de dados relacional que define e padroniza elementos de dados e a relação deles entre si. Os dados são armazenados em linhas, com cada linha representando uma única instância de algo (por exemplo, um cliente). Essas linhas são bem compreendidas devido ao esquema da tabela, que explica o que cada campo na tabela representa. Isso facilita a consulta de dados estruturados. **Dados estruturados são quentes, imediatamente prontos para serem analisados.**

  A desvantagem dos dados estruturados é a falta de flexibilidade. Digamos que você decidiu que deseja acompanhar a idade dos seus clientes. Você deve reconfigurar o esquema para permitir esse novo dado e considerar todos os registros que não têm um valor para esse novo campo. Não é impossível, mas pode ser um processo muito demorado.

  Exemplos de aplicativos de dados estruturados incluem Amazon RDS, Amazon Aurora, MySQL, MariaDB, PostgreSQL, Microsoft SQL Server e Oracle.

* **Dados semistruturados**:  
  Dados semiestruturados são armazenados na forma de elementos em um arquivo. Esses dados são organizados com base nos elementos e atributos que os definem. Eles não estão em conformidade com modelos ou esquemas de dados. Os dados semiestruturados são considerados como tendo uma estrutura autodescritiva. Cada elemento é uma única instância de alguma coisa, como uma conversa. Os atributos dentro de um elemento definem as características dessa conversa. Cada elemento de conversa pode monitorar atributos diferentes. Isso torna os dados semiestruturados bastante flexíveis e capazes de escalar para atender às demandas dinâmicas de uma empresa com mais rapidez do que os dados estruturados. **Dados semiestruturados são mornos. Alguns estarão prontos para uso e outros podem precisar de limpeza ou pré-processamento**

  A diferença é a análise. Pode ser mais difícil analisar dados semiestruturados quando os analistas não conseguem prever quais atributos estarão presentes em um determinado conjunto de dados.

  Exemplos de datastores semiestruturados são CSV, XML, JSON, Amazon DynamoDB, Amazon Neptune e Amazon ElastiCache.

* **Dados não estruturados**:  
  Dados não estruturados são armazenados na forma de arquivos. Esses dados não estão em conformidade com um modelo de dados predefinido nem organizados de maneira predefinida. Dados não estruturados podem ser arquivos de texto, fotografias, gravações de áudio ou até mesmo vídeos. Dados não estruturados estão cheios de informações irrelevantes, o que significa que os arquivos precisam ser pré-processados para fazer avaliaçãos significativas. Isso pode ser feito de várias maneiras. Por exemplo, os serviços podem adicionar tags aos dados com base em regras definidas para os tipos de arquivos. Os dados também podem ser catalogados para deixá-los disponíveis a serviços de consulta. **Dados não estruturados são um oceano congelado, repleto de tudo o que você precisa, mas separado por todo tipo de coisa de que você não precisa**

  Exemplos de dados não estruturados incluem e-mails, fotos, vídeos, dados de clickstream, Amazon S3 e Amazon Redshift Spectrum.

### Introdução a datastores estruturados

Os dados estruturados são classificados como dados armazenados em um banco de dados ou em um sistema de gerenciamento de banco de dados (DBMS ou SGBD). Um banco de dados é um conjunto estruturado de dados mantido em um computador, que pode ser acessado de várias maneiras. Um DBMS fornece estrutura aos dados, capacidade de manter os dados durante todo o ciclo de vida e capacidade de gerenciar interações com outros processos e sistemas. Diferentes sistemas de gerenciamento de banco de dados gerenciam a organização de dados de diferentes maneiras para atingir metas específicas, como avaliação complexa, navegação rápida de relacionamentos ou recuperação do estado da sessão.

### Dados de arquivos de texto puro

Em geral, os dados de arquivos de texto puro residem em uma planilha. Pode não parecer um banco de dados, mas ele atende a todos os requisitos básicos. Esse formato fornece uma base sólida para entender algumas das considerações ao escolher um DBMS.

Algumas das falhas mais comuns: valores duplicados, valores ambíguos, dados ausentes, relacionamentos.

### Bancos de dados relacionais

O armazenamento de arquivos de texto puro pode não atender às suas necessidades de armazenamento de dados estruturados. A próxima etapa lógica é migrar para uma solução mais robusta: um banco de dados relacional.

Um processo conhecido como normalização ajuda uma empresa a transformar dados de arquivos de texto puro em um banco de dados relacional. A normalização é um conjunto de regras que funcionam juntas para reduzir a redundância, aumentar a confiabilidade e melhorar a consistência do armazenamento de dados.

Um banco de dados relacional é criado para armazenar dados estruturados para que possam ser coletados, atualizados e consultados facilmente. Bancos de dados relacionais dependem de uma série de estruturas, chamadas de tabelas, para armazenar os dados coletados. Essas tabelas são navegadas usando a linguagem de consulta estruturada ou SQL.

![Bancos de dados relacionais](imagens/4.png)

Logicamente, tabelas de banco de dados relacional agrupam dados com base em uma pessoa, um local, uma coisa ou um evento relacionado a esses dados. Esses agrupamentos são chamados de entidades. Cada entidade é armazenada como uma tabela. 

Uma coluna, conhecida como campo, é usada para descrever um atributo da entidade. Uma linha, conhecida como registro, na tabela representa uma única instância de uma entidade.

Pense em uma planilha, em que cada linha tem uma célula para cada coluna. Cada célula pode conter um valor. As regras dentro do esquema definem se o atributo é obrigatório ou opcional. As relações são criadas primeiramente garantindo que cada linha em uma tabela seja exclusiva. Isso é feito criando uma chave primária. Esse valor de chave primária pode ser usado para criar relações entre tabelas. Uma chave externa é um campo que usa os valores de uma chave primária em outra tabela para definir um registro na tabela atual. Essa ação é o que cria a relação. Alguns mecanismos de banco de dados podem impor essa relação para garantir que apenas os valores da chave primária possam ser usados na chave externa.

**Vantagens:**

- A conformidade com ACID;
- Os dados são facilmente armazenados, editados e recuperados usando uma linguagem SQL comum;
- A estrutura pode ser aumentada verticalmente com rapidez.
  
**Desvantagens**

- A dificuldade no armazenamento de dados não estruturados;
- As consultas podem ficar lentas devido às complexas exigências de agrupamento;
- O esquema pode dificultar o aumento da quantidade.


O principal benefício de um banco de dados relacional usando SQL é ser uma tecnologia comprovada amplamente adotada e compreendida. Há menos risco envolvido com um banco de dados relacional, especialmente devido à conformidade com ACID e a uma grande comunidade de especialistas na área. Há uma expectativa de latência transacional muito boa, especialmente em hardware adequadamente dimensionado, e bancos de dados relacionais são considerados perfeitos para o OLTP para conjuntos de dados relativamente pequenos.

Existem preocupações de escalabilidade com um banco de dados relacional. À medida que os conjuntos de dados crescem, a única maneira de manter o desempenho é aumentar as capacidades de hardware dos servidores que executam o aplicativo. Outro problema importante é o esquema fixo de bancos de dados relacionais. É difícil fazer alterações sem interrupções nas arquiteturas básicas de banco de dados, o que pode afetar os tempos de desenvolvimento de novas funcionalidades.

### Introdução a datastores semiestruturados e não estruturados

### Bancos de dados não relacionais

Bancos de dados não relacionais são criados para armazenar dados semiestruturados e não estruturados de uma forma que ofereça rápida coleta e recuperação. Existem várias categorias amplas de bancos de dados não relacionais e os dados são armazenados em cada um para atender a requisitos específicos.

### Comparação de bancos de dados relacionais e não relacionais

![Comparação de bancos de dados relacionais e não relacionais](imagens/5.png)  

## Veracidade: limpeza e transformação

**Definições**

**Curadoria** é a ação ou o processo de selecionar, organizar e cuidar de itens em uma coleção.
**Integridade dos dados** é a manutenção e a garantia de precisão e consistência dos dados durante todo o seu ciclo de vida.
**Veracidade dos dados** é o grau em que os dados são exatos, precisos e confiáveis.

Os dados sofrem alterações ao longo do tempo. À medida que são transferidos de um processo para outro, e por um sistema e outro, há oportunidades para que a integridade dos dados seja afetada negativamente. Você deve garantir a manutenção de um alto nível de certeza de que os dados que está analisando são confiáveis.

### Compreensão da integridade dos dados

A integridade dos dados tem a ver com garantir que seus dados sejam confiáveis.

### Definições

**Limpeza de dados** é o processo de detecção e correção de corrupções nos dados.
**Integridade referencial** é o processo para garantir que as restrições das relações da tabela sejam impostas.
**Integridade do domínio** é o processo para garantir que os dados inseridos em um campo correspondam ao tipo de dados definido para esse campo.
**Integridade da entidade** é o processo para garantir que os valores armazenados em um campo correspondam às restrições definidas para esse campo.

### Identificação de problemas de integridade dos dados

Os dados podem ser provenientes de fontes internas e externas. É altamente improvável que você possa ter influência sobre dados gerados fora da sua empresa. No entanto, dentro da sua empresa, você pode conseguir fazer recomendações sobre melhorias para as origens dos dados com as quais estará interagindo.

Quando alterar a maneira como os sistemas de origem ingerem dados não for uma opção, geralmente é responsabilidade do analista de dados determinar a integridade da origem dos dados em questão e fazer ajustes para considerar qualquer área em que essa fonte possa estar sem integridade.

Algumas das práticas recomendadas para ajudar a identificar problemas de integridade dos dados:
- **Saber qual deve ser a limpeza**:  
  Antes de fazer qualquer outra coisa, você deve ter consenso sobre o resultado limpo. Algumas empresas consideram dados limpos os dados em seu formato bruto com regras empresariais aplicadas. Algumas empresas consideram dados limpos os dados que foram normalizados, agregados e tiveram substituições de valor aplicadas para regular todas as entradas. Esses são dois entendimentos muito diferentes de limpeza. Verifique qual é a sua meta.
- **Saber de onde os erros vêm**:  
  À medida que você encontrar erros nos dados, rastreie a origem provável. Isso ajudará a prever cargas de trabalho que terão problemas de integridade. Isso também ajudará você a justificar alterações no sistema que melhorariam a eficiência das operações de ETL.
- **Saber quais são as alterações aceitáveis**:   
  Sob uma perspectiva unicamente centrada em dados, inserir um zero em uma coluna vazia pode parecer uma decisão de limpeza de dados fácil, mas é preciso saber quais os efeitos dessa alteração. Da mesma maneira, combinar os números de inventário “Em pedido” e “Em estoque” nos relatórios mensais pode parecer inconsequente. No entanto, esses dados podem acabar nas mãos de um gerente de inventário que agora acredita que há um problema de perda de inventário. Esses são os pequenos detalhes que podem causar um impacto negativo enorme.  
- **Saber se os dados originais têm valor**:  
  Em alguns sistemas, os dados originais não têm mais valor depois de terem sido transformados. No entanto, em dados altamente regulamentados ou dados altamente voláteis, é importante que tanto os dados originais quanto os dados transformados sejam mantidos no sistema de destino.

### Esquema de informações

Um esquema de informações é um banco de dados de metadados que armazena informações sobre os objetos de dados em um banco de dados. O Microsoft SQL Server chama seu esquema de informações de banco de dados mestre. A Oracle usa tabelas de dicionário de dados e um registro de metadados. O Apache Hadoop usa um metastore. Cada DBMS pode ter nomes diferentes para a estrutura de dados que armazena os metadados, mas a finalidade é a mesma: definir quais são todos os objetos no banco de dados e registrar informações vitais sobre eles. Esses bancos de dados armazenam informações como o nome e o tamanho de uma tabela, os índices na tabela e as restrições de dados na tabela. As configurações de segurança para usuários, ativos de dados externos e configurações de gerenciamento também podem ser incluídas.

Dadas as permissões apropriadas no banco de dados, você pode consultar o esquema de informações para saber mais sobre os objetos no banco de dados. Quando as consultas são executadas, essas informações são usadas para garantir a melhor otimização para a consulta. O esquema de informações também pode ser usado na manutenção do próprio banco de dados.

### Compreensão da consistência do banco de dados

**Conformidade com o ACID**

ACID é o bastião de longa duração da integridade dos dados relacionais. Em um banco de dados como o Amazon RDS, uma sequência de instruções executadas em conjunto é chamada de transação. Milhões de transações podem ser executadas consecutivamente. Os dados e as restrições nesses dados são muito ativos em bancos de dados relacionais.
*ACID é um acrônimo para Atomicidade, Consistência, Isolamento e Durabilidade. É um método para manter a consistência e a integridade em um banco de dados estruturado.*  
O objetivo de um banco de dados compatível com ACID é retornar a versão mais recente de todos os dados e garantir que os dados inseridos no sistema atendam a todas as regras e restrições atribuídas em todos os momentos.

**Conformidade com BASE**

O BASE promove a integridade de dados em bancos de dados não relacionais, às vezes são chamados de bancos de dados NoSQL. Bancos de dados não relacionais, como o Amazon DynamoDB, ainda usam transações para processar solicitações. Esses bancos de dados são hiperativos e a principal preocupação é a disponibilidade dos dados em relação à consistência dos dados. Para garantir que os dados estejam altamente disponíveis, as alterações nos dados são disponibilizadas imediatamente na instância em que a alteração foi feita. No entanto, pode levar algum tempo para que essa alteração seja replicada em toda a frota de instâncias. O objetivo é que a alteração acabe sendo totalmente consistente em toda a frota.
*BASE é um acrônimo para BAsicamente disponível, eStado flexível, Eventualmente consistente. É um método para manter a consistência e a integridade em um banco de dados estruturado ou semiestruturado.*

### Transações do Amazon DynamoDB

Em novembro de 2018, a Amazon apresentou as transações do Amazon DynamoDB. Esse recurso implementa a conformidade com ACID em uma ou mais tabelas dentro de uma única conta e região AWS. Você pode usar transações ao criar aplicativos que exijam inserções, exclusões ou atualizações coordenadas de vários itens como parte de uma única operação empresarial lógica.

### Introdução ao processo de ETL 

Extração, transformação e carregamento (ETL) é o processo de coletar dados de origens brutas e transformá-los em um tipo comum. Esses novos dados são carregados em um local final para serem disponibilizados para avaliação e inspeção analíticas. Em ambientes modernos baseados na nuvem, geralmente nos referimos a esse processo como ELT (extração, transformação e carregamento). As etapas são simplesmente executadas em uma ordem diferente, mas o resultado é o mesmo.

### Serviços AWS no processo de ETL

A AWS fornece serviços para cada fase do processo de ETL. Do armazenamento da origem dos dados aos relatórios, a AWS cobre todos os aspectos.  

![Serviços AWS no processo de ETL](imagens/6.png)  

**Transformação de dados - comparação entre o Amazon EMR e o AWS Glue**

Quando se trata de executar o componente de transformação de dados do ETL, há duas opções na AWS: o Amazon EMR e o AWS Glue. Esses dois serviços fornecem resultados semelhantes, mas exigem diferentes quantidades de conhecimento e investimento de tempo.

O **Amazon EMR** é uma abordagem mais prática para criar seu pipeline de dados. Esse serviço fornece uma plataforma robusta de coleta e processamento de dados. Para usar esse serviço, sua equipe deve ter sólido conhecimento técnico e know‑how. A vantagem dele é que você pode criar um pipeline personalizado para atender às suas necessidades de negócios. Além disso, os custos de infraestrutura podem ser menores do que executar a mesma carga de trabalho no AWS Glue.

O **AWS Glue** é uma ferramenta de ETL gerenciada sem servidor que oferece uma experiência muito mais simplificada do que o Amazon EMR. Isso torna o serviço ideal para tarefas simples de ETL, mas você não terá tanta flexibilidade quanto teria com o Amazon EMR. Você também pode usar o AWS Glue como um metastore para seus dados transformados finais usando o AWS Glue Data Catalog. Esse catálogo é uma substituição de uma metastore do Hive.
