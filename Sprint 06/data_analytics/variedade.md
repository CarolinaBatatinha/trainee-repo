## Variedade: estruturas e tipos de dados

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