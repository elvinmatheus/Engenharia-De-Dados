# Spark com Databricks

## Spark

- Ferramenta de Processamento de Dados Distribuído em um Cluster
- Em memória
- Veloz
- Escalável
- Particionamento

- Escala horizontalmente - Cluster

### Replicação / Tolerância a Falha

- Dados são copiados entre os nós do cluster. Isso traz o benefício de, entre outras coisas, tolerância a falhas

### Particionamento

### Spark vs Python, R ou Banco de Dados

- Spark tem arquitetura voltada a processar dados
  - Melhor performance, porém:
    - Não substitui Python
	- Não substitui SQL ou um SGBD relacional

### Linguagens

- Scala
- Python
- Java
- R
- SQL

### Por que Spark?

- Aprendemos a processar dados, criar modelos, etc. com Python e R, utilizando bibliotecas como Pandas, Scikit Learn, etc.
- Precisamos de Spark?
  - Alta performance pela sua natureza "distribuída"

- Temos tudo com Python e Spark com Pyspark

## Arquitetura e Componentes

### Componentes

- Machine Learning (Mlib)
- SQL (Spark SQL)
- Processamento em Streaming
- Processamento de Grafos (GraphX)

### Spark SQL

- Permite ler dados tabulares de várias fontes (CSV, JSON, Parquet, ORC, etc)
- Pode usar sintaxe SQL

### Streaming: Spark Structured Streaming

- Dados estruturados

### Grafos acíclicos dirigidos

- Spark constrói gráficos acíclicos dirigidos

### Elementos 

- SparkSession: Sessão
- Application: Programa

### Transformações e Ações
- Um DataFrame é imutável: traz tolerância a falha
- Uma Transformação gera um novo data frame
- O processamento de Transformação só ocorre de fato quando há uma Ação: Lazy Evaluation
