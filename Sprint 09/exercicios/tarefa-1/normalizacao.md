A normalização é um processo que visa organizar e otimizar a estrutura de um banco de dados, garantindo que os dados sejam armazenados de forma eficiente e mantendo a consistência e integridade dos dados.

O primeiro passo é **identificar as entidades** presentes nos dados fornecidos. Nesse caso, identificamos as seguintes entidades: Carro, Cliente, Vendedor e Locação.

Na sequência, aara cada entidade identificada, **são identificados os atributos associados** (por exemplo, para a entidade *tb_carro*, podemos ter atributos como *idCarro*, *kmCarro* e *marcaCarro*).

Em seguida, são **analisadas as relações entre as entidades** para determinar como elas se conectam. Isso inclui identificar as chaves estrangeiras que relacionam as tabelas entre si. 

A seguir, **as tabelas são normalizadas**, removendo redundâncias e organizando-as de forma a reduzir a duplicação de dados e manter a integridade referencial. Isso envolve dividir as tabelas em estruturas mais granulares, conforme necessário, e garantir que cada tabela represente uma única entidade ou relação.

Posteriormente são **criadas as tabelas normalizadas**, assegurando que cada tabela esteja em uma forma normalizada adequada, podendo envolver a criação de novas tabelas e/ou modificação das existentes para atender aos requisitos de normalização.

Por fim, são **configuradas as restrições de integridade referencial** (*como chaves primárias e estrangeiras*) para garantir a consistência e a integridade dos dados entre as tabelas.