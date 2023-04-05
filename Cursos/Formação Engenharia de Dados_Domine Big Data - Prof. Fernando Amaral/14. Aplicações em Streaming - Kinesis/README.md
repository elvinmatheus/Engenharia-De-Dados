# Aplicações em Streaming

## AWS Kinesis: visão geral

- Kinesis é uma alternativa gerenciada do Apache Kafka
- Logs de aplicações, IOT, clickstreams
- Dados em "tempo real"

- Kinesis Streams: Ingestão de streaming com baixa latência e em grande escala (streams de dados)
- Kinesis Analytics: Executa análise de tempo real em streams usando SQL (Análise de Dados)
- Kinesis Data Firehouse: Carrega streams no S3, Redshift, ElasticSearch e Splunk (streams de entrega)

- Streams são divididos em Shards ordenados / Partições
- Shards podem ser provisionados com antecedência (ou serveless)
- Retenção de dados é de 24 horas por padrão, pode chegar a 7 dias
- Capaz de reprocessar dados
- Várias aplicações podem consumir o mesmo stream
- Uma vez que os dados são inseridos no Kinesis, não pode ser excluído (imutabilidade)
- Registros podem ter até 1 MB de tamanho

### Limites de dados no Kinesis Data Streams

- Produtores
  - 1MB por segundo ou 1000 mensagens na escrita por Shard
  - Ou então "ProvisionedThroughputException"
- Consumidor clássico:
  - 2MB/s de leitura por Shard entre todos os consumidores
  - 5 chamadas de API por segundo por shard entre todos os consumidores
- Retenção de dados
  - 24 horas por padrão
  - Pode ser estendido

### Kinesis Data Firehouse

- Serviço totalmente gerenciado, sem administração
- Próximo ao tempo real (mínimo de 60 segundos de latência para batches não completos)
- Ingestão de dados no Redshift / Amazon S3 / ElasticSearch / Splunk
- Escala automaticamente
- Suporte a muitos formatos de dados
- Conversão de dados de CSV / JSON para Parquet / ORC (apenas para o S3)
- Transformação de dados através do AWS Lambda (ex: CSV => JSON)
- Suporta compressão quando usa o Amazon S3 (GZIP, ZIP e SNAPPY)
- Paga-se pela quantidade de dados que entra no Firehouse

### Kinesis Data Streams vs Firehouse

- Streams
  - Pode escrever código customizado (produtor / consumidor)
  - Tempo real (~70ms ~200ms de latência)
  - Deve gerenciar escalabilidade (divisão / merge de shard)
  - Armazenamento de dados de 1 a 7 dias, capacidade de replay, múltiplos clientes

- Firehouse
  - Totalmente gerenciado, envia para S3, Splunk, Redshift, ElasticSearch
  - Serveless: transformação com Lambda
  - Próximo a tempo real (menor tempo de buffer é 1 minuto)
  - Escala automaticamente
  - Não tem armazenamento de dados
