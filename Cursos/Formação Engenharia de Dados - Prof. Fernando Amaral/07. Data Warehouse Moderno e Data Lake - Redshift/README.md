# Data Warehouse Moderno e Data Lake

## Modelo Dimensional

- Idealizado nos anos 90
- Focado em Negócio: Fatos
- Fácil modelagem
- Fácil sumarização de fatos (medidas)
- Dados limpos
- Apenas informação estritamente necessária
  - Custo de armazenamento
- Otimização baseada em índices

## Modelo dimensional hoje

- Custo de armazenamento é quase insignificante
- Custo de Processamento baixou: Calcular Dimensões e Medidas sob demanda pode ser melhor do que tratar e armazenar dados em um modelo "Star"
- Uma tabela desnormalizada é muito mais fácil de ser compreendida e consultada do que um modelo "Star"
- São um modelo em desuso, mas estarão ativos por décadas

## Data Lakes e Data Lakehouses

- Otimizados para processar grandes volumes de dados
- Desacoplados
- Baseados em SQL e Tabelas
- Mais amigáveis
- Menor custo

- HIVE, Snowflake, Redshift, Big Query

## Redshift

- Solução de DW na nuvem: AWS
- Para processar grandes volumes de dados
- Orientado a Coluna
- Baseado em versão do PostgreSQL
  - Possui semelhança em sintaxe SQL, mas é um produto completamente diferente
- Não a maioria das restrições de integridade referencial, como chaves estrangeiras e unique

### Orientado a Coluna

- Colunas são armazenadas individualmente
- Valores são armazenados de forma contínua
- Criar uma linha requer recuperar valores de várias colunas

#### Orientado a linha VS Orientado a coluna

- Orientado a linha
  - Ler uma coluna requer a leitura de todas
  - Uma linha pode ter vários tipos, então a compressão é menor
  - Ler todas as colunas tem um custo menor
  - Inserir ou atualizar colunas tem um custo menor

- Orientado a coluna
  - Ler uma coluna, requer a leitura apenas da coluna
  - A coluna tem um mesmo tipo, então tem maior compressão
  - Ler todas as colunas tem um custo alto
  - Inserir ou atualizar colunas tem um custo maior
