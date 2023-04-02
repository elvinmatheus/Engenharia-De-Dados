# Armazenamento de Dados distribuído

## Armazenamento de Arquivos

- Não se trata apenas de um repositório de documentos!
- Dados "vivos" são mantidos em sistemas de arquivos
- Apresentam características como:
  - Versionamento
  - Segurança: controle de acesso, criptografia, etc.
  - Ciclo de vida
- Características relacionadas a "Big Data":
  - Particionamento
  - Escalabilidade
- Exemplos
  - S3
  - HDFS
  - Azure Blob Storage

## Visão Geral do AWS S3

- O Amazon S3 permite que aas pessoas armazenem objetos (arquivos) em buckets
- Buckets devem ter um nome único global
- Objetos (arquivos) tem uma chava. A chave é o caminho completo:
  - <bucket>/vendas.csv
  - <bucket>/pasta1/pasta2/vendas.csv
- Isso é útil e interessante quando olharmos partições
- Tamanho máximo de um objeto é de 5TB
- Tags de Objetos (chave/valor, até 10), úteis para segurança e ciclo de vida

## AWS S3 para Ciência de Dados 

- Backbone para muitos serviços de ML do AWS (ex.: SageMaker)
- Criar um Data Lake
  - Tamanho infinito, sem provisionamento
  - Durabilidade: 99,999999999%
  - Armazenamento (S3) desacoplado do processamento (EC2, Amazon Athen, Amazon Redshift, Spectrum, Amazon Rekognition e AWS Glue)
- Arquitetura centralizada
- Armazenamento de objetos: suporta qualquer tipo de arquivo
- Formatos comuns para Engenharia de Dados: CSV, JSON, Parquet, ORC, Avro, Protobuf

## AWS S3: Particionamento

- Padrões para acelerar consultas em intervalos (ex.: AWS Athena)

- Por data: s3://<bucket>/vendas/ano/mes/dia/hora/venda_00.csv
- Por produto s3://<bucket>/vendas/234565/venda_00.csv
- Podemos definir qual estratégia de particionamento escolher
- O particionamento de dados pode ser feito pelas próprias ferramentas do AWS (Glue)

## AWS S3 - Camadas

- Amazon S3 Standard - Uso geral
- Amazon S3 - Acesso Infrequente (IA)
- Amazon S3 One Zone - Acesso infrequente
- Amazon S3 - Camada Inteligente
- Amazon Glacier

## Regras de Ciclo de Vida do S3

- Conjunto de regras para mover os dados entre diferentes camadas, para reduzir custo de armazenamento
- Exemplo: Uso geral => Uso Infrequente => Glacier

- Ações de transição: objetos fazem a transição para outra classe de armazenamento. Ex:
  - Mover objetos da classe padrão IA depois de 60 dias da criação
  - E mover para o Glacier para arquivamento depois de 6 meses

- Ações de Expiração: O S3 exclui objetos expirados para nós
  - Logs de acesso podem ser configurados para exclusão depois de um tempo

## Criptografia S3 para Objetos

- Existem quatro métodos de criptografia para objetos no S3

- SSE-S3: Criptografa objetos S3 usando chaves criadas e gerenciadas pelo AWS
- SSE-KMS: Usa o serviço de Gestão de Chaves do AWS para gerenciar chaves criptográficas
  - Segurança adicional (usuário deve ter acesso a chave KMS)
  - Trilha de auditoria para uso da chave KMS
- SSE-C: quando queremos gerenciar nossas próprias chaves
- Criptografia no cliente

- De uma perspectiva de análise de dados, SSE-S3 e SSE-KMS são usadas

## Segurança S3

- Baseada no usuário
  - Políticas IAM - quais chamadas de API devem ser permitidas para usuários específicos

- Baseada em Recursos
  - Políticas de Buckets: regras abrangentes de buckets - permitem contas cruzadas
  - Lista de controle de acesso a objetos (ACL) - controle mais detalhado
  - Lista de controle de acesso ao Bucket (ACL) - menos comum

## Políticas de Buckets S3

- Políticas baseada em configuração JSON
  - Recursos: buckets e objetos
  - Ações: definir API para permitir ou negar
  - Efeito: permite / nega
  - Principal: A conta ou usário que aplica a política

- Use a política de Bucket S3 para
  - Dar acesso público a um bucket
  - Forçar objetos a serem criptografados no upload
  - Dar acesso a outra conta (conta cruzada)

## Segurança S3 - Outros

- Rede - VPC Endpoint Gateway:
  - Permite que o tráfico fique dentro de sua VPC (ao invés de ir para a internet pública)
  - Garante que seus serviços privados (AWS SageMaker) possam acessar o S3

- Log e auditoria
  - Logs de acesso do S3 podem ser armazenados em outro bucket s3
  - Chamadas de API podem ser logadas na "AWS CloudTrail"

- Baseados em Tags (combina políticas IAM e políticas do bucket)
  - Exemplo: adicionar a tag Classificatin=PHI a seus objetos.
