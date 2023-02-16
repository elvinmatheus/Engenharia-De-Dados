# 1. O que é a Engenharia de Dados?

A Engenharia de Dados é responsável por **manter**, **desenvolver**, **testar**, **consolidar (extrair/ingerir)** e **garantir a disponibilidade** de estruturas de dados.

**1.1 Manter**

Quanto a:

- Disponibilidade;
- Confiabilidade;
- Segurança;
- Planejamento;
- Monitoramento.

**1.2 Desenvolver**

- Data Warehouses;
- Data Lakes;
- Processos de Análise (Batch);
- Streaming;
- Processos de ETL e ELT.

**1.3 Testar**

Quanto a:

- Performance;
- Requisitos Funcionais;
- Requisitos de governança de dados;
- Segurança.

**1.4 Consolidar: **Extrair/Ingerir**

Consolidar dados de diversas fontes:

- Data Warehouses;
- Data Lakes.

**1.5 Garantir a Disponibilidade**

- Sistema em produção:
  - Segurança;
  - Privacidade;
  - Acesso;
  - Monitoramento;
  - Planos de Contigência.

**1.6 Em resumo...**

> "Um Engenheiro de Dados é o profissional que desenvolve, opera e mantém estruturas de dados complexas e heterogêneas, sendo o responsável pela segurança, integridade, disponibilidade e confiabilidade destes"

**1.7 DBA vs Engenheiro de Dados**

- Tradicionalmente o DBA é responsável por sistemas Transacionais e Dimensionais

- O Engenheiro de Dados tem sob sua tutela uma gama maior de ferramentas e modelos de dados

**1.8 Cientistas de Dados vs Engenheiro de Dados**

O cientista de dados é responsável por:

- Modelos de Machine Learning;
- Artefatos de Visualização;
- Preparação de dados para modelos;
- Busca de padrões/outliers;
- Automação de tarefas preditivas.

# 2. O que é Big Data?

**2.1 Conceito**
São dados produzidos de acordo com os 5 "V's": velocidade, volume, variedade, veracidade e valor.

**2.2 Conceito II**

> Big Data é o fenômeno da massificação de elementos de produção e armazenamento de dados, bem como os processos e tecnologias para extraí-los e analisá-los.
– Introdução à Ciência de Dados, de Fernando Amaral

**2.3 Causas**

- Barateamento e Miniaturização da Tecnologia;
- Facilidade de Coletar e Armazenar Dados;
- Evolução Tecnológica;
- Mudanças Sociais;
- Internet;
- Dispositivos Conectados (IOT).

# 3. Estruturas de Dados

- Dados Estruturados;
- Dados Semiestruturados;
- Dados não Estruturados.

**3.1 Dados Estruturados**

- Armazenado em uma mesma estrutura;
- Estrutura Rígida;
- Exemplo: Tabela de SGBD, Planilha Eletrônica.

**3.2 Dados Semiestruturados**

- Estrutura heterogênea
- Não estão completamente não estruturados. Existe uma estrutura representada.
- Evolutiva: mais fácil sua estrutura mudar.

Exemplos:

- XML;
- JSON;
- RDF - Resource Description Framework;
- OWL - Web Ontology Language.

**3.3 Dados Não Estruturados**

- Sem estrutura definida, nem de forma implícita;
- Sem metadados ou descrição da estrutura;
- Corresponde à maioria dos dados existentes;
- Formato que mais cresce.

Exemplos:

- Vídeos;
- Imagens;
- Páginas de Internet;
- Recibos eletrônicos;
- E-mails;
- Tweets;
- Documentos em Geral.

Formatos:

- Chave-valor
- Texto: ex.: CSV
- ORC: arquivo em colunas ou linhas, chave-valor
- AVRO: serializado
- PARQUET: colunas aninhadas

**3.4 Arquitetura de Dados**

- Ambiente Transacional
  - Produção e Guarda;
    - Registrar fatos;
	- Recuperar registros.
- Ambiente Analítico
  - Armazenamento e Análise;
    - Manter Histórico;
	- Analisar dados;
  - Não há produção.

# 4. Conceitos

**4.1 Cluster**

- Computação Distribuída;
- Cada computador é chamado nó;
- Computadores operando em conjunto, conectados, com o mesmo objetivo (processar dados) = Dividir para Conquistar;
- Podem estar dispersos fisicamente, inclusive em diferentes continentes;
- Pode estar no mesmo hack;
- Podem ser virtualizados;
- Estrutura Master/Slave:
  - Master: coordena, distribui, agenda;
  - Slave: armazena, processa.

**4.2 Replicação vs Partição**
- Replicação: dados são copiados;
- Partição: dados são divididos;
- Replicação e Partição: dados são divididos e copiados.

**4.3 Tipos de Partição**
- Centralizada:
  - Serviço central gerencia os dados nas partições. Possui todos os metadados;
	- Pode ser um gargalo para o sistema.
  - Range:
    - Divide em intervalor;
	- Pode ficar desbalanceado.
  - Hash:
	- Usa uma Hash Table para distribuir os dados de forma balanceada entre os nós.

**4.4 Mutation**
- Suporte ao sistema em alterar dados;
- Em sistemas distribuídos isso pode não ser tão simples;
- Alguns formatos de arquivo, como colunas, o processo também pode ser complexo.

**4.5 Data Warehouse vs Data Lake**
- Data Warehouse (Clássico)
  - Implementado a partir dos anos 90;
  - Estruturado;
  - Dimensional.
- Data Lake
  - Big Data;
  - Todo tipo de informação;
  - Hadoop/HDFS.

**4.6 Batch vs Streaming vs Interativo**
- Batch: dados são coletados (extraídos, tratados, armazenados) e processados. Podem levar horas, semanas, meses...
- Streaming: dados processados em tempo real, a medida que são produzidos. Saída em tempo real ou próximo ao tempo real. Processamento constante (Fluxo);
- Interativo (Ad Hoc): Interface onde processamento é requerido e o resultado é analisado.

- Exemplo:
  - Batch: Sistema de busca de produtos de varejo on-line: milhões de termos pesquisados por dia. Diariamente, os dados são processados para criar um ranking das palavras mais buscadas;
  - Streaming: Sistema de busca de produtos de varejo on-line: Avaliação de transação de pagamentos é fraudulenta. As transações são processadas a medida que são executadas;
  - Interativo (Ad Hoc): Rodar uma consulta para ver as vendas do dia de determinado produto.

**4.7 Tipos de Streaming**
- Native: dados são processados assim que chegam, sem esperar por demais dados;
- Micro-batching: dados são agrupados e processados em grupo (delay).



