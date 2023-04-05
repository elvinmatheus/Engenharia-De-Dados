# Introdução ao Ecossistema Hadoop

## Introdução

- Hadoop
  - Solução para processamento massivo de grandes volumes de dados
  - Ecossistema construído em sua base
  - Vem perdendo espaço para soluções mais modernas e pela adoção de aplicações em Nuvem
  - Ainda é importante para um Engenheiro de Dados

### Map Reduce

- Dividir tarefas de processamento de dados em vários nós
  - Dados são divididos em blocos
  - Divisão de problemas grandes e/ou complexos em pequenas tarefas

### Map e Reduce

- Escalável
- Tolerante a falhas
- Disponibilidade
- Confiável
- Usa o conceito de chave/valor
- Não cria gargalos na rede, pois dados não trafegam (processamento no nó)

### Importante

- Processamento em Batch
- Grande volume de dados
- Processamento distribuído
- Linguagem Imperativa (Java)

### Dados podem ser copiados pro HDFS

- Uma vez no HDFS, podem ser acessados por diversos sistemas (Hadoop, Hive, Spark, etc)

### MapReduce

- Mapeamento é executado em paralelo nos nós
- Apenas quando Mapeamento é encerrado, redução inicia, também em paralelo
- Fase intermediária: Shuffle
- Existem tarefas que requerem apenas a etapa de Mapeamento

## MapReduce

### Hadoop

- Processamento em Batch
- Baseado no conceito de MapReduce
- Desenvolvido em Java
- Open source
- Distribuído
- Hardware commodity
- Capaz de distribuir o processamento em dezenas ou milhares de nós em um cluster
- Suporte a dados estruturados ou não estruturados
- Terabytes até Petabytes de dados

#### Master / Slave

- Opera no conceito Master/Slave
- Master:
  - Gestão: mantém metadados, logs, adiciona, encontra, exclui e copia arquivos, distribui as tarefas de mapeamento e redução entre os nós, agendamento, balanceamento, etc.
- Slaves:
  - Mantém dados, replica blocos

- Master:
  - NameNode: faz a gestão do HDFS em um nó: mantém metadados, logs, adiciona, encontra, exclui e copia arquivos
  - JobTracker: distribui as tarefas de mapeamento e redução entre os nós
  - TaskTracker: recebe as tarefas de mapeamento e redução do JobTracker: agendamentos, balanceamento de carga, gestão de falhas, etc.
- Slaves:
  - DataNodes: mantém dados, replica blocos

- NameNode pode ser replicado (Hadoop 2)
- DataNodes são configurados em modo ativo e standby
- Heartbeat: enviado do DataNode ao NameNode regularmente, como sinal de "saúde"

### Yarn

- Alocação de recursos de forma global e unificada no cluster
- Agendamentos
- Priorização
- Tolerância a falhas
- Componentes:
  - ResourceManager: um por cluster
    - ApplicationManager: gerencia atividade, otimização, distribuição de recursos, etc.
	- Scheduler
  - NodeManager: um por nó
    - Responsável pela execução dos Jobs
  - Application Master:
    - Distribui tarefas ao containers
  - Container: mantém as tarefas

## HDFS

- Hadoop Distributed File System

### O que é um sistema de arquivos?

- Faz o gerenciamento de arquivos em disco:
  - Mantém integridade
  - Segurança
  - Privacidade
  - Metadados

### Sistemas de arquivos

- Windows: FAT, NTFS
- Linux: EXT2, EXT3, EXT4, XFS, JFS
- MacOS: APFS, HFS PLUS

### Por que não usar NTFS ou Ext3?

- Porque o Hadoop precisa de um gerenciamento com características diferenciadas:
  - Arquivo separado em blocos
  - Distribuídos em nós de redes
  - Cópias replicadas

### Tipos de Arquivos

- Texto: padrão em ferramentas como Hive
- Sequence File: Chave-valor binário // Podem ser divididos ou unidos facilmente
- AVRO: formato binário para serialização // Ótimo para troca de dados
- ORC: colunar otimizado para consulta de linhas // formato "favorito" do ecossistema Hadoop
- RC: orientado a coluna, chave-valor // alta taxa de compressão em linha
- Parquet: orientado a colunas // Binário

## Limitações do Hadoop

- Hadoop vs Big data: "sinônimos"

- Hadoop não é bom para:
  - processamento Real-Time
  - pequenos volumes de dados
  - problemas complexos (grafos)
  - acesso interativo (*ad hoc*) e operações simples
  - operações que precisem de grande tráfego de dados em uma rede
  - problemas transacionais
  - não quer programação (Java)

- Insuperável para:
  - Grandes volumes de dados...
  - Processamento em batch
