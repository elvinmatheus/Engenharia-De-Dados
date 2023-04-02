# Aspectos Gerais sobre Engenharia de Dados

## Data Lakes

- Armazém corporativo de dados
- "Simples", disponível, acessível, seguro
- Em conformidade com Governança de Dados
- Versão "Big Data" do Data Warehouse clássico
- Normalmente em Hadoop/HDFS
- Dados estruturados/não estruturados/semi-estruturados

### Estruturas

- Landing Layer - dados brutos
- Analytic Layer - dados tratados para consumo
- Arquivamento - dados históricos

### Camadas

- Aquisição - extração (ingestão)
- Processamento
- Consumo

### Ingestão de Dados

- Capturar dados para o Data Lake
  - Batch
  - Real-time - CDC - Chance Data Capture

## Tipos de Projetos

- ETL
- Processamento de Dados
- Aplicações

### Testes

- Automação de testes (Selenium, Katalon Studio, etc)
- Chaos Monkey - ferramenta que introduz falhas para testar a resiliencia

### Build e Deploy

- Automação minimiza riscos
  - Jenkins
  - Gestão de Configuração com Puppet ou Chef
  - Container como Docker

### Solução Desacoplada

- Solução modular e desacoplada 
  - Banco de Dados
  - ETL
  - Auditoria
  - Monitoramento
  - Frontend

### Definir Métricas Mínimas de Performance

- Tempo de Resposta
- Throughput
- Capacidade de Carga

## Agil vs Tradicional

Quando não usar agil?

- Cliente ou questões de conformidade não permitem
- Requisitos precisam estar definidos no início do projeto
- Se o patrocinador precisa entender todo o projeto antes de aprovar
- Quando o projeto é muito grande
- Quando a equipe está dispersa

## Segurança

### Autenticação e Autorização

- Autenticação - garantir que o usuário é quem ele alega ser
- Autorização - garantir que o usuário acesse dados dos quais ele tem permissão
- HDFS pode operar sem nenhum tipo de autenticação e autorização ou pode usar LDAP, Active Directory, Kerberos e X.509
- Kerberos pode autenticar usuários e nós

### Kerberos

- Serviço de autenticação em ambiente distribuído
- Faz a mediação entre cliente e servidor usando autenticação TTP - Trusted Third Party
- Kerberos authenticator server (AS) - fornece credenciais, armazena as chaves
- Servidor de concessão de tickets (Ticket Granting Server - TGS) - fornece credenciais para serviços específicos
- Servidor de Administração (KADM) - Administra as chaves privadas

### Data At Rest

- HDFS oferece criptografia transparente, feita pea aplicação
- Zonas criptografadas - diretórios, arquivos e subdiretórios
- Dados podem ser acessados diretamente no HDFS, sem passar pelas camadas de autenticação e autorizaçãode aplicações
- Pode ser estendida para dados em transito
- Hadoop Key Management Server (KMS) - gestão de chaves

### Apache Ranger

- Framework para monitorar e gerir segurança de dados na plataforma Hadoop
- Permite gestão por produto (Hive, Storm, HBase, etc) e por recurso (arquivos, pastas) por grupos e usuários
- Possui funcionalidades de auditoria

### Comunicação entre Nós

- Por padrão a comunicação entre nós e as aplicações clientes não é criptografada
- Recomendação é usar SSL ou TSL

### Auditoria e Logs

- Scribe - serviço de agregação de logs do Facebook
- LogStach - serviço de ingestão e transformação de logs da Elastic
- Log4J - Fundação Apache, usado por aplicativos em Java

### Outros Aspectos

- Inclusão de nós e novos software servidor
- APIs

### Apache Sentry

- Solução granular e modular de Segurança para o Ecossistema Hadoop
- Plugins para Hive, Solr, Impala e HDFS
- Composto por
  - Sentry Server
  - Data Engine (ex. Hive)
  - Sentry Plugin

## Riscos

### Análise de Viabilidade

Uma POC pode criar um MVP (minimal viable product)

- Prova de Conceito - fração do que será desenvolvido
- Protótipo - tenta simular todo o sistema ou grande parte dele
- Piloto - sistema oficial é implementado e testado

### Medidas

### Modelos

- Taxa de acerto atende o negócio?
- Existem atributos suficientes para treinar o modelo?
- Existe dados com qualidade mínima?

### Expectativas de Tempo não Realistas

### Segurança e Privacidade

### Os requisitos de cultura e idioma estão claros? São suportados pelas ferramentas?

### Existe um plano de testes?

### Imaturidade

- Hype Cycle (Gartner)

- Technology Trigger - Período de incubação
- Peak of Inflated Expectations - promessas de um produto maravilhoso, estável, altamente funcional
- Trough of Dissillusionment - usuários começam a engrentar problemas diversos (segurança, integração, disponibilidade)
- Slope of Enlightenment - começa a ser usado em maior volume e se estabilizar
- Plateau of Productivity - o produto se consolida

### O projeto entrega valor?

### Os critérios de sucesso estão claros?

### O projeto está em conformidade com as diretivas de Governança de Dados da Organização/Legislação?

### A infraestrutura necessária ao projeto é conhecida?

- O projeto preve o crescimento da solução? A solução é escalável?

### Quais são os requisitos de disponibilidade?

### Os requisitos de qualidade do projeto são conhecidos, consensuais e factíveis?

### Manuais de implantação, manutenção estão planejados?

### Existe um plano para avaliar a qualidade de dados?

### Existe um plano de limpeza e tratamento de dados?

### Todas as fontes de dados do projeto foram identificadas?

### Todas as fontes de dados do projeto são acessíveis?

### As fontes de dados possuem documentação apropriada?

### A latencia entre a produção da informação e carga é suficiente/viável para a produção de valor?

### Orçamentos Inadequados (foi planejado um orçamento para contigencias?)

### As necessidades de aquisições são conhecidas?

### O tempo para entregas pelos fornecedores é conhecido e atende os requisitos do projeto?

### Os critérios de seleção de fornecedores estão estabelecidos?

### é possível responder questões dos prováveis fornecedores?

### Existem no mercado profissionais com as competencias identificadas?

### Todas as competencias para o projeto foram identificadas?

### Falta de envolvimento

### Existe um plano para capacitação de usuários finais?

### Existe um plano de evangelização das partes interessadas

## Big Data na Nuvem

### Infraestrutura

- Softwares
- Gerenciados de banco de dados
- Dados
- Sistema Operacional
- Servidores
- Armazenamento
- Rede
- Segurança
- Backup

### Opções

- Cloud vs On-Primeses vs Híbrido

#### On-Primeses

- Controle total
- Altos investimentos
  - Segurança, Hardware,
- Implantação, configuração, atualização
- Espaço Ocupado
- Licença e controle de licenças de software
- Suporte
- Disponibilidade menor
- Escalabilidade difícil

#### Cloud

- Sujeito a SLAs
- Hardware Commodities
- Escalabilidade fácil
- Configuração e Atualização transparente
- Pode contratar backup, segurança, redundancia
- Sem custos com licenças
- Sem grandes investimentos

#### IaaS vs PaaS vs SaaS

- On-Primeses
- IaaS - Infrastructure as a Service - AWS, Azure
- PaaS - Platform as a Service - AWS Elastic Beanstalk, Windows Azure, Google App Engine
- SaaS - Software as a Service - Google Apps
- Cloud

## Ciencia de dados

### Aspectos de Ciencia de Dados

- Machine Learning
  - Classificação
  - Agrupamentos
  - Regras de Associação
- Reinforcement Learning
- Busca e Otimização
- Algoritmos Genéticos
- Sistemas Especialistas
- Lógica Difusa
- Processamento de Linguagem Natural

### Machine Learning

- Capacidade do Computador Aprender com Dados
  - Classificação
  - Agrupamentos
  - Regras de Associação

### Classificação

- Classificar um elemento em uma categoria
  - Classificar uma transação como fraude
  - Definir a espécie de uma planta
  - Classificar um cliente como bom ou mal pagador
  - etc

### Redes Neurais Artificiais

### Agrupamentos

- Agrupa elementos semelhantes, de acordo com o grau de semelhança e o algoritmo utilizado

### Regras de Associação

- Busca associação entre itens

### Reinforcement Learning

- Como deve agir um agente de IA, em um ambiente, a fim de solucionar um problema?

- Proposta
  - Método de tentativas com acertos e error
  - Recompensas por acertos

### Busca e Otimização

- Existem problemas computacionais que (ainda) não foram resolvidos com uma equação ou fórmula. E preciso buscar uma possível solução entre todas as soluções possíveis (espaço de busca)

### Algoritmos Genéticos

- Buscam imitar o processo da Evolução das Espécies
- Simplificado, porém eficiente
- Aplicado em problemas de busca, otimização, agendamento, etc.

- Diferenças
  - Na natureza, não existe condição de parada

### Sistemas Especialistas

- Ausencia de dados
  - Problema novo
  - Sigilo

- Sistemas especialistas são utilizados para reduzir a incerteza

- Sistemas Especialistas são um sistema de informação que buscam emular a capacidade de decisão de um perito no assunto
- Aplicação Limitada a uma área específica do conhecimento
- Capaz de aprender
- Heurístico
  - Não possui resposta pronta e exata, busca aproximação
- Alta disponibilidade
- Baixo Custo
- Duração Infinita
- Replicável

#### Aplicações

- Diagnóstico médico
- Diagnóstico de mal funcionamento de sistema ou equipamento
- Agendamento
- Decisões financeiras
- Monitoramento de processos
- Classificação
- Segurança pública
- Mudanças Climáticas

### Lógica Difusa

- Metodologia de tomada de decisão e resolução de problemas que simula o pensamento humano

- Qualquer valor real entre 0 e 1
- Verdade ou associação "Parcial";
  - Muito baixo, baixo, médio, alto, muito alto...

### Processamento de Linguagem Natural

- Interpretação ou produção de linguagem humana por computador

#### Aplicações

- Tradução
- Respostas e perguntas
- Analise de sentimentos
- Correção ortográfica
- OCR
- Reconhecimento de Fala
- Sintetização da Fala
- Previsão de digitação
- Classificação de documentos
- Resumos
