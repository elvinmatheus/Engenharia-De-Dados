# Introdução 

## O que é a Engenharia de Dados?

A Engenharia de Dados é responsável por **manter**, **desenvolver**, **testar**, **consolidar (extrair/ingerir)** e **garantir a disponibilidade** de estruturas de dados.

**Manter**

Quanto a:

- Disponibilidade;
- Confiabilidade;
- Segurança;
- Planejamento;
- Monitoramento.

**Desenvolver**

- Data Warehouses;
- Data Lakes;
- Processos de Análise (Batch);
- Streaming;
- Processos de ETL e ELT.

**Testar**

Quanto a:

- Performance;
- Requisitos Funcionais;
- Requisitos de governança de dados;
- Segurança.

**Consolidar: **Extrair/Ingerir**

Consolidar dados de diversas fontes:

- Data Warehouses;
- Data Lakes.

**Garantir a Disponibilidade**

- Sistema em produção:
  - Segurança;
  - Privacidade;
  - Acesso;
  - Monitoramento;
  - Planos de Contigência.

**Em resumo...**

> "Um Engenheiro de Dados é o profissional que desenvolve, opera e mantém estruturas de dados complexas e heterogêneas, sendo o responsável pela segurança, integridade, disponibilidade e confiabilidade destes"

### DBA vs Engenheiro de Dados

- Tradicionalmente o DBA é responsável por sistemas Transacionais e Dimensionais

- O Engenheiro de Dados tem sob sua tutela uma gama maior de ferramentas e modelos de dados

### Cientistas de Dados vs Engenheiro de Dados

O cientista de dados é responsável por:

- Modelos de Machine Learning;
- Artefatos de Visualização;
- Preparação de dados para modelos;
- Busca de padrões/outliers;
- Automação de tarefas preditivas.

## O que é Big Data?

### Conceitos

São dados produzidos de acordo com os 5 "V's": velocidade, volume, variedade, veracidade e valor.

### Conceito II

> Big Data é o fenômeno da massificação de elementos de produção e armazenamento de dados, bem como os processos e tecnologias para extraí-los e analisá-los.
– Introdução à Ciência de Dados, de Fernando Amaral

### Causas

- Barateamento e Miniaturização da Tecnologia;
- Facilidade de Coletar e Armazenar Dados;
- Evolução Tecnológica;
- Mudanças Sociais;
- Internet;
- Dispositivos Conectados (IOT).

## Estruturas de Dados

- Dados Estruturados;
- Dados Semiestruturados;
- Dados não Estruturados.

### Dados Estruturados

- Armazenado em uma mesma estrutura;
- Estrutura Rígida;
- Exemplo: Tabela de SGBD, Planilha Eletrônica.

### Dados Semiestruturados

- Estrutura heterogênea
- Não estão completamente não estruturados. Existe uma estrutura representada.
- Evolutiva: mais fácil sua estrutura mudar.

Exemplos:

- XML;
- JSON;
- RDF - Resource Description Framework;
- OWL - Web Ontology Language.

### Dados Não Estruturados

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

### Arquitetura de Dados

- Ambiente Transacional
  - Produção e Guarda;
    - Registrar fatos;
	- Recuperar registros.
- Ambiente Analítico
  - Armazenamento e Análise;
    - Manter Histórico;
	- Analisar dados;
  - Não há produção.

## Conceitos

### Cluster

- Computação Distribuída;
- Cada computador é chamado nó;
- Computadores operando em conjunto, conectados, com o mesmo objetivo (processar dados) = Dividir para Conquistar;
- Podem estar dispersos fisicamente, inclusive em diferentes continentes;
- Pode estar no mesmo hack;
- Podem ser virtualizados;
- Estrutura Master/Slave:
  - Master: coordena, distribui, agenda;
  - Slave: armazena, processa.

### Replicação vs Partição

- Replicação: dados são copiados;
- Partição: dados são divididos;
- Replicação e Partição: dados são divididos e copiados.

### Tipos de Partição

- Centralizada:
  - Serviço central gerencia os dados nas partições. Possui todos os metadados;
	- Pode ser um gargalo para o sistema.
  - Range:
    - Divide em intervalor;
	- Pode ficar desbalanceado.
  - Hash:
	- Usa uma Hash Table para distribuir os dados de forma balanceada entre os nós.

### Mutation

- Suporte ao sistema em alterar dados;
- Em sistemas distribuídos isso pode não ser tão simples;
- Alguns formatos de arquivo, como colunas, o processo também pode ser complexo.

### Data Warehouse vs Data Lake

- Data Warehouse (Clássico)
  - Implementado a partir dos anos 90;
  - Estruturado;
  - Dimensional.
- Data Lake
  - Big Data;
  - Todo tipo de informação;
  - Hadoop/HDFS.

### Batch vs Streaming vs Interativo

- Batch: dados são coletados (extraídos, tratados, armazenados) e processados. Podem levar horas, semanas, meses...
- Streaming: dados processados em tempo real, a medida que são produzidos. Saída em tempo real ou próximo ao tempo real. Processamento constante (Fluxo);
- Interativo (Ad Hoc): Interface onde processamento é requerido e o resultado é analisado.

- Exemplo:
  - Batch: Sistema de busca de produtos de varejo on-line: milhões de termos pesquisados por dia. Diariamente, os dados são processados para criar um ranking das palavras mais buscadas;
  - Streaming: Sistema de busca de produtos de varejo on-line: Avaliação de transação de pagamentos é fraudulenta. As transações são processadas a medida que são executadas;
  - Interativo (Ad Hoc): Rodar uma consulta para ver as vendas do dia de determinado produto.

### Tipos de Streaming

- Native: dados são processados assim que chegam, sem esperar por demais dados;
- Micro-batching: dados são agrupados e processados em grupo (delay).

### Conceitos de Streaming

- Event = dado
- Producer = gerador
- Subscriber = consome

### Latencia

- Intervalo de tempo entre a produção da informação e seu processamento
  - Em batch = alta latencia
  - Streaming = baixa latencia

### Real Time e Near Real Time

- Real Time = em tempo real
- Near Real Time = próximo ao tempo real

- Normalmente quando fala-se Real Time, refere-se a Near Real Time

### Processamento Distribuído

- Um processamento em batch / streaming / memória pode ou não ser distribuído

### Commodity Hardware

- Commodity Hardware
  - Barato
  - Compatível
  - Amplamente Disponível
  - Intercambiável

### Sistemas Resilientes

- Uma das características de sistemas resilientes - tolerante a falhas - é ser capaz de continuar operando mesmo sob alguma falha.

### Sistemas Distribuídos

- Replicação = dados são copiados
- A replicação dos dados é um aspecto de Sistemas Resilientes
- A replicação dos dados ocorre quando tem-se falhas em
  - Rede
  - Software
  - Etc.
  - Disco Rígido (média de falas em discos rígidos por ano = 4.81%)

### Change Data Capture

- Capturar mudanças nos dados transacionais a partir do log de transação
  - Incremental = carga de mudanças
    - Síncrono = captura a medida que as mudanças ocorrem
	- Assíncronos = captura em intervalos
  - Bulk = carga de todos os dados

### Disponibilidade

- Riscos
  - Falhas de Software
  - Falhas de Hardware
  - Falhas de Rede
  - Ataques
  - Erros humanos
  - Upgrades

### Fault Tolerance

- Tolerância a Falhas
- Garantias que um sistema, em caso de falha, continuará operando

- Executer Recover = tolera falha em slave, que é replicado
- Full

### State Management

- Em caso de falha, o sistema manterá o estado na recuperação
  - Sem manter estado = o processo (ex. ingestão de dados) é reiniciado
  - Com manutenção de estado, ele continua de onde parou

### Cloud e On-Primese

- Cloud pode trazer custos menores (TCO)

### ETL e ELT

- ETL: Extract, Transform and Load
- ELT: Extract, Load and Transform

### Metadados

- Dados de Dados
  - Tipo
  - Precisão
  - Restrições

### Data at Rest vs Data at Wire

### Orientado a Coluna ou Linha

- Orientado a linha comprime por grupos de linhas (blocos)
- Mais eficiente para escrita e leitura
  - Desvantagem - baixa taxa de compressão
  - Leitura de algumas colunas - precisa ler todas

- Orientado a Colunas
  - Armazena-se colunas separadamente
  - Maior taxa de compressão
  - Melhor para leitura

### Modelos de Dados

- Operacional (manter operações)
  - Transacional/OLTP
  - SQL / NoSQL
- Analítico (apoio a decisão)
  - Data Warehouse
  - Data Lake
  - OLAP

- Operacional
  - Produz dados
  - Consulta, Inclusão, Exclusão, Atualização
  - Não mantém histórico
  - Redundancia mínima ou nula
  - Pode ter grande volume
  - Objetiva Integridade
  - Orientado a processo

- Analítico
  - Carrega dados produzidos de várias fontes
  - Inclusão e Consulta
  - Mantém histórico
  - Redundancia
  - Volume sempre maior
  - Objetiva Informação de Qualidade
  - Orientado a negócio

### CAP Theorem

- Usado no design de sistemas distribuídos
- Importantíssimo para Engenharia de Dados
- Proposto pelo cientista Eric Brewer no final dos anos 80

**Impossível ter mais de 2**

- Um sistema de dados distribuído só pode garantir 2 de 3 propriedades
  - Consistência - todos os nós na rede retornam a mesma versão dos dados
  - Disponibilidade - todos os nós respondem a leituras e escritas em um tempo razoável
  - Partição tolerante a falhas - o sistema continua a funcionar, mesmo tendo perdido dados entre os nós
