# Fundamentos de NoSQL

## Introdução NoSQL

- Conjunto de produtos cujas restrições, presentes no modelo relacional, são flexibilizadas:
  - Desnormalizado
  - Sem restrições de integridade
  - Modelo transacional mais flexível

- Os produtos buscam resolver problemas específicos de certas aplicações, que eram mais difíceis de resolver no modelo relacional:
  - Processamento eficiente
  - Paralelismo
  - Escalabilidade
  - Custo

### Quatro tipos principais

- Key-Value Database (KVP)
- Colunas Ordenadas
- Banco de Dados de Documentos
- Banco de Dados Grafos

#### Key-Value Pair (KVP)

- Armazena conjunto Chave/Valor
- Em memória, disco ou híbrido
- Produtos: redis, amazon DynamoDB, Couchbase

#### Colunas Ordenadas

- Dados orientados em colunas. Cada linha tem um ponteiro.
- Armazenado de maneira contínua
- Tolerante a falhas através de sistema de arquivo distribuído
- Baseado no modelo Bigtable (Google)
- Produtos: Apache HBASE, Hypertable

#### Banco de Dados de Documentos

- Não é um sistema de ECM (Enterprise Content Mangement)
- Exemplo: suporte a JSON
- Produtos: mongoDB, CouchDB

#### Banco de Dados Grafos

- Aplicações em redes sociais, medicina, genética, RH, etc.
- Produtos: Neo4j
### Exemplos de Aplicações

- Sessão de usuários em Aplicações Web
- Conteúdo como e-books, artigos e documentos em geral
- Agregação ou Repositório Central de Dados
- Plataformas de Anúncios Direcionados
- EHR (Electronic Healthcare Records)
- Análise de Série Temporal
- Dados do crachá sociométrico

### Ranking

- Relacional: Oracle
- Key-value: Redis
- Documento: MongoDB
- Grafo: Neo4j
- Colunas ordenadas: Cassandra

fonte: db-engines.com/en/ranking

## Key-value pair

- Também conhecido como hash ou dicionário

### Key-value Database 

- Conjunto chave-valor
  - A chave pode ser produzida automaticamente ou inserida
  - Value pode ser um texto, documento JSON, etc.
  - A chave é única e aponta para um documento
  - A chave é responsável pela recuperação do registro
  - Bucket: grupo lógico de chaves
  - Não existe tipo de dado pré-definido

## Colunas Ordenadas

- Conhecido também como Wide Column Store, Column Oriented Database, etc.
- Dados armazenados em colunas, não em linhas
- Keyspace: equivalente a schema do relacional: agrupa
- Column families: equivalente a uma tabela do relacional: dados
- Column Family: várias linhas
- Cada linha pode conter diferentes números de colunas, não precisa have uma equivalência
- Cada coluna contém uma chave/valor mais data e hora
- Cada linha tem uma chave única

### Modelo

- No modelo de colunas, cada coluna é armazenada em um arquivo fisicamente separado
- O gerenciador de banco de dados, precisa carregar apenas a coluna da consulta
- É um ótimo modelo para compressão (mais dados repetidos por linhas), reduzindo espaço de armazenamento

## Banco de Dados de Documentos

- Armazenam chave/valor
- Diferente do Key Value Pair, o valor é um documento estruturado e indexado, com metadados
- Valor (Documento) pode ser consultado

### JSON

- JSON: JavaScript Object Notation
- Feito para troca de dados
- Mais compacto e legível que XML

- Estrutura nome/valor, entre aspas duplas
- Dados separados por vírgula
- Chaves separam objetos
- Vetores entre colchetes

- Tipos:
  - String
  - Número
  - Vetor
  - Booleano
  - Nulo
  - Objeto

## Grafos

- Armazenam Nós e Vértices

### Aplicações

- Conectar pessoas e Analisar suas Relações
- Combate ao terrorismo
- Colaboração entre equipes
- Analisar Redes de Comunicação
- Achar rotas
- Tráfego de Redes
- Prever a disseminação de doenças
- Linguística e Processamento de Linguagem Natural
- Estudo de moléculas
