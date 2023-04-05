# ETL e Data Crawler - Glue e Athena

## Glue

- Serviço gerenciado de ETL
- Baseado em Spark

### Construir um Data Lake

- Schema de dados na Origem e Destino
- Conectar a Origem e Destino
- Transformar dados

### Crawler

- Conecta em fontes de dados para definição de schema
- Cria metadados no Glue "Data Catalog"

### Connector

- Informações necessárias para conexões com fontes de dados

### Glue Job

- Processo de ETL
- Geralmente:
  - Origem
  - Transformações
  - Destino
- Executados
  - Sob demanda
  - Agenda
  - Gatilhos

### Data Catalog

- Data Catalog
  - Repositório de Metadados
- Database
  - Agrupa logicamente tabelas
  - Não cria, nem carrega dados
- Tables
  - Representações de metadados de dados tabulares
  - Dados mantêm sua forma e fonte original

## Objetivo

- Criar um datalake com dados de vendas para consultas
- Fonte: Arquivos CSV

### O que vamos fazer

- Criar IAM role
- Glue
  - Criar banco de dados
  - Criar e executar crawler
    - Criar tabelas associadas ao Banco de Dados: Glue Data Catalog
  - Criar e executar Job
    - Transformar dados:
	  - Tratamento de nomes de campos
	  - Joins
	  - Salvar no S3 como parquet com partição (Status)
  - Criar Banco de Dados e Crawler para o Data Lake
- Athena
  - Configurar Athena para realizar consultas no Data Lake
