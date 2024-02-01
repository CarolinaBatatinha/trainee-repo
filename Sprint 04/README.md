# Relatório da Sprint 4
Fizeram parte da quarta sprint a conclusão do curso de Python entitulado "Python 3 - Curso Completo do Básico ao Avançado" (*onde foi tratado sobre a programação funcional*), **Docker para Desenvolvedores (*com Docker Swarm e Kubernetes*)** e **Estatística Descritiva com Python**.

## Programação Funcional com Python

"Python 3 - Curso Completo do Básico ao Avançado", onde foi tratado sobre a programação funcional, abordando sobre funções de primeira classe, funções de alta ordem, closure, funções lambda, map, filter, reduce, imutabilidade e generators. Nessa sprint também doi foram solicitadas as resoluções de exercícios an plataforma da Udemy. Os códigos desenvolvidos na resolução estão disponíveis nos links abaixo.

- [x] [Exercício 1](exercicios/ex01.py)
- [x] [Exercício 2](exercicios/ex02.py)
- [x] [Exercício 3](exercicios/ex03.py)
- [x] [Exercício 4](exercicios/ex04.py)
- [x] [Exercício 5](exercicios/ex05.py)
- [x] [Exercício 6](exercicios/ex06.py)
- [x] [Exercício 7](exercicios/ex07.py)


## Estatística Descritiva com Python

A estatística descritiva é uma ferramenta essencial para entender e resumir características fundamentais dos dados. Abaixo serão explorados alguns dos conceitos mencionados anteriormente e como eles podem ser aplicados em Python.

### 1. Medidas de Tendência Central:
**Média**:
A média é uma medida central que representa o valor médio de um conjunto de dados. Pode ser calculada usando a função np.mean() do NumPy.
```python
import numpy as np
dados = np.array([1, 2, 3, 4, 5])
media = np.mean(dados)
print(f'Média: {media}')
```

**Mediana**:
A mediana é o valor que divide os dados ordenados ao meio. Ela é menos sensível a valores extremos do que a média.
```python
mediana = np.median(dados)
print(f'Mediana: {mediana}')
```

**Moda**:
A moda é o valor que ocorre com mais frequência nos dados. A biblioteca SciPy fornece a função mode() para calcular a moda.
```python
from scipy.stats import mode
moda = mode(dados).mode[0]
print(f'Moda: {moda}')
```

### 2. Medidas de Dispersão:

**Desvio Padrão e Variância:**
O desvio padrão e a variância medem a dispersão dos dados em torno da média.

```python
desvio_padrao = np.std(dados)
variancia = np.var(dados)
print(f'Desvio Padrão: {desvio_padrao}')
print(f'Variância: {variancia}')
```

**Amplitude**:
A amplitude é a diferença entre o valor máximo e mínimo nos dados.
```python
amplitude = np.ptp(dados)
print(f"Amplitude: {amplitude}")
```

### 3. Medidas de Forma:

**Assimetria**:
A assimetria mede a simetria da distribuição dos dados.
```python
from scipy.stats import skew
assimetria = skew(dados)
print(f"Assimetria: {assimetria}")
```

**Curtose**:
A curtose mede a "afiamento" da distribuição em relação à normal.
```python
from scipy.stats import kurtosis
curtose = kurtosis(dados)
print(f"Curtose: {curtose}")
```

### 4. Visualização de Dados:
**Histogramas**:
Os histogramas são gráficos que mostram a distribuição dos dados.

```python
import matplotlib.pyplot as plt
plt.hist(dados, bins=10, edgecolor='black')
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.show()
```
**Boxplots**:
Os boxplots oferecem uma representação visual dos quartis e identificação de *outliers*.

```python
plt.boxplot(dados)
plt.title('Boxplot')
plt.show()
```
Esses são apenas alguns aspectos da estatística descritiva, mas eles fornecem uma base sólida para a análise de dados. O **Python**, com suas bibliotecas especializadas, é uma ferramenta poderosa para realizar análises estatísticas em conjuntos de dados de forma eficiente e eficaz.

## Docker

O **Docker** é uma plataforma de código aberto que automatiza a implantação, o dimensionamento e a gestão de aplicações em containeres. Containeres são unidades leves e portáveis que empacotam software e todas as suas dependências, permitindo que ele seja executado de maneira consistente em diversos ambientes.

Com o **Docker**, é possível criar, distribuir e executar aplicativos em containeres de maneira eficiente. Cada container é uma instância isolada que contém o aplicativo e suas dependências, garantindo consistência e facilitando a implantação em diferentes ambientes, como desenvolvimento, teste e produção.

A diferença entre container e imagem, ambos recursos fundamentais no Docker, é que uma ***imagem*** é como um modelo ou um snapshot que contém todas as informações necessárias para executar um aplicativo, enquanto um ***container*** é uma instância em execução dessa imagem.

As *principais vantagens* do **Docker** incluem:

* **Portabilidade**: Os containeres podem ser executados em qualquer lugar onde o Docker esteja instalado, independentemente do sistema operacional ou infraestrutura subjacente.

* **Isolamento**: Os containeres isolam aplicativos e suas dependências, evitando conflitos entre diferentes ambientes.

* **Eficiência**: Containeres compartilham o kernel do sistema operacional hospedeiro, tornando-os mais leves e rápidos em comparação com máquinas virtuais tradicionais.

* **Escalabilidade**: facilitando a escala de aplicativos, permitindo a replicação de containeres para atender a demandas crescentes.

* **Automatização**: O Docker fornece ferramentas para automatizar a criação, distribuição e execução de containeres, simplificando o ciclo de vida do aplicativo.

Alguns exemplos dos comandos mais comuns:

1. docker run:

* Cria e inicia um contêiner a partir de uma imagem.
```bash
docker run -d --name meu-container nginx
```
2. docker ps:
   
* Lista os contêineres em execução.
```bash
docker ps
```

3. docker pull:
   
* Baixa uma imagem do Docker Hub.
```bash
docker pull ubuntu
```

4. docker build:

* Constrói uma imagem a partir de um Dockerfile.
```bash
docker build -t minha-imagem:1.0 .
```

5. docker stop e docker start:

* Para e reinicia um contêiner em execução.
```bash
docker stop meu-container
docker start meu-container
```

6. docker exec:

* Executa um comando dentro de um contêiner em execução.
```bash
docker exec -it meu-container bash
```

7. docker rm:

* Remove um contêiner.
```bash
docker rm meu-container
```

8. docker rmi:

* Remove uma imagem.
```bash
docker rmi minha-imagem:1.0
```

9. docker ps -a:

* Lista todos os contêineres, incluindo os que estão parados.
```bash
docker ps -a
```

10. docker-compose:

* Utilizado para definir e executar aplicativos Docker multi-container.
```bash
docker-compose up -d
```

11. docker logs:

* Exibe os logs de um contêiner.
```bash
docker logs meu-container
```

12. docker network:

* Permite gerenciar redes Docker.
```bash
docker network create minha-rede
```

Além disso, nessa sprint precisamos resolver um [desafio](desafio/Dockerfile) envolvendo conceitos de Docker e Python.