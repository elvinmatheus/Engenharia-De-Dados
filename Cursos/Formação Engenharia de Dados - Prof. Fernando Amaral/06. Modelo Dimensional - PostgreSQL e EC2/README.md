# Modelo Dimensional

## Modelo Gerencial

### Armazéns de Dados (Data Warehouse)

- Dados consolidados de várias fontes
- Informação histórica, de 3 a 10 anos
- Otimizado para consulta
- Operação de Inclusão e Consulta apenas
- Desnormalizado: Não íntegro, redundante
- Modelo Dimensional

### Data Mart

- Banco de Dados Analítico Departamental

### Data Warehouse

- Conjunto de Data Marts, reúne todos os dados de apoio à decisão da organização

### OLAP

- Sistemas Analíticos, ou Online Analytical Processing é a capacidade para manipular e analisar um grande volume de dados sob múltiplas perspectivas

## Granulidade

- O nível de detalhamento em que a informação gerencial é armazenada é conhecido como "grão"
- Do ponto de vista gerencial, a informação não precisa vir detalhada. O detalhe normalmente é fornecido através de relatórios, com finalidade de conferência, extraído do sistema Transacional, para a área operacional.

- Decisão importante do projeto

- Também é precio ter o nível necessário para apoiar a tomada de decisão

- Mais detalhes...
  - Maior volume de dados
  - Maior tempo de carga
  - Mais infraestrutura
  - Mais tempo de processamento
  - Mais lento (usuário)

## Data Warehouse

### Construção do DW

- Construir um DW é um processo complexo, requer mão de obra especializada e pode levar anos:
  - Entender do negócio
  - Compreender as estruturas de dados na sua origem
  - Desenvolver processos de transformação destes dados

### Por que DW?

- Um ambiente analítico não deve interferir no ambiente de transações
- Os dados no ambiente transacional não estão em formato apropriado para análise
- Normalmente, dados de várias fontes devem ser consolidados para gerar informação gerencial

### BI

- Conjunto de Ferramentas, Tecnologias e processos para Análise de Dados

### Relatório

- Informação Detalhada
- Estática, sem interatividade
- De caráter operacional
- Principal função: conferência
- Pode estar agrupada
- Pode conter elementos gráficos
- Apresenta totais por grupo, página, relatório, entre outros

### Cubo

- Permite aumentar ou reduzir o nível de detalhe da informação, aplicar filtro, agrupar, etc
- Sua forma elementar é textual, porém a maioria das ferramentas permite produzir gráficos
- Um cubo apresentar um fato
- Dimensões nos eixos verticais e horizontais
- Medidas ao Centro

### Dashboard

- Painel visual
- Informação Resumida
- Gerencial, Operacional ou Estratégico
- Oferece características de Navegação
- Não traz detalhes, mas pode fornecer "Tops"
- Pode conter KPI

### Problemas

- Diferentes plataformas e arquiteturas
- Bancos de dados inacessíveis
- Qualidade de dados e estruturas de dados
- Falta de Documentação
- Desconhecimento do negócio

## Modelos Dimensionais e Cubos

### Dados Multidimensionais

- Dados que podem ser vistos sob diversas perspectivas, de forma dinâmica, cujas medidas são calculadas automaticamente conforme sua estrutura

### Cubos

- Cubos OLAP

## Cubo

## Drills

- Drill Down
- Drill Up
- Drill Across
- Slice
- Dice
- Gráficos

## Fatos

- O Fato é o dado central, é o tema do qual se quer analisar
- Dimensões: são os diversos pontos de vista sobre o qual se quer analisar o fato. Uma dimensão tempo é obrigatória
- Medidas: são valores que serão analisados

### Modelagem Multidimensional

#### Fato

- É o assunto central
- Agrega medidas (na mesma tabela) e n dimensões

#### Relacionamento N:n

## Dimensões

- Sempre relacionadas a um (ou mais) fatos
- Formas de visualizar a informação

- Fato
  - Quando?
  - Quem?
  - O quê?
  - Como?
  - Onde?

## Dimensão Tempo

- Ano
  - Semestre
    - Trimestre
	  - Mês
	    - Dia da semana

## Hierarquia e Compartilhamento

### Hierarquia de Dimensões

- Ano > Mês > Trimestre > Dia
- País > Estado > Cidade > Bairro
- Categoria > Sub Categoria > Produto

### Dimensões Compartilhadas

## Medidas

- Características Numéricas
- São atributos na Fato
- Podem envolver cálculos complexos

- Aditivas: podem ser operadas matematicamente. Ex.: quantidade de vendas
- Não Aditivas: não podem ser operadas matematicamente. Ex.: percentual de vendas
- Semi-aditivas: podem ser operadas matematicamente, mas de maneira não uniforme. Ex.: Balanços

- Fato > Quanto?
  - Quando?
  - O que?
  - Quem?
  - Como?
  - Onde?

- Podem ser calculadas no processo de carga
- Podem ser calculadas dinamicamente pelo Servidor OLAP
- Podem ser calculadas pela ferramenta de visualização
- Pode conter hierarquias de cálculos

## Chave Substituta

- Um Cliente possui uma Chave Primária no Modelo Relacional
- Um Cliente pode ser carregado n vezes no Modelo Dimensional

## Slow changing Dimension, Modelos, Mascaradas

### SCD

- Slowly Changing Dimensions type 2

- Outros tipos:
  - 0: Mantém original
  - 1: Sobrescreve
  - 3: Cria novo atributo

### Dimensões com Validade ou Status

- Dimensões podem receber um atributo de validade, indicando o período em que estavam válidas
- Ainda um Status
- Usado para fins de recarga dos dados transacionais ou recálculo

### Dimensões Mascaradas

- Ao invés de entidades, implementamos um atributo no fato
- Usar para dimensões que possuem um número fixo de opções (ex.: sexo do cliente)

### Dimensões Degeneradas

- Dimensão que deriva da tabela fato
- Não tem sua própria "tabela" de dimensão
- Usada quando precisamos manter o mesmo grão do sistema transacional
- Ex.: número da nota, número do pedido

### Dimensões Junk

- Situações em que existem vários atributos do tipo Sim/Não, zero ou um, Ativo ou Inativo, etc.
- Uma dimensão Lixo deve reunir todos estes atributos em uma mesma tabela.

### Star

### Snow Flake

## KPIs e BSC

### BI

- O que aconteceu
- O que está acontecendo
- O que vai acontecer (ML etc)

### KPI

- Mede o "sucesso" da empresa em determinada área
- O "sucesso" é medido diante de algum objetivo estabelecido

## Dez regras Essenciais

- The 10 Essential Rules of Dimensional Modelling
  1. Carregue dados atômicos e detalhados na estrutura dimensional
  2. Estruture modelos dimensionais a partir de processos de negócios
  3. Garanta que cada tabela fato tenha uma dimensão de data relacionada
  4. Garanta que todos os fatos em uma mesma tabela fato tenham o mesmo nível de grão
  5. Resolva relações muito para muitos nas tabelas fato
  6. Resolva relações um para muitos em tabelas dimensões
  7. Armazene rótulos e valores de filtros em tabelas dimensão
  8. Tenha certeza que tabelas dimensões usam uma chave substitura
  9. Crie dimensões compartilhadas para integrar dados por toda a empresa
  10. Avalie os requisitos continuamente e garanta entregar uma solução de DW/BI que é aceita pelos usuários de negócio e que suporta suas tomadas de decisão

## ETL

- ETL: Extract, Transform, Load (Extração, Transformação, Carga) são ferramentas de software cuja função é a extração de dados de diversos sistemas, transformação desses dados conforme regras de negócios e a carga dos dados.

- Etapa mais difícil, longa e cara na construção de um DW

### Estratégia de ETL

- Conectar em horários apropriados
- Extrair os dados necessários
- Desconectar
- Conexões somente leitura

### ETL

- No uso clássico, ETL extrai dados de sistemas Transacionais, transforma o modelo de dados, e carrega no Armazém de Dados

### Ferramentas de ETL

- Muitas ferramentas diferentes
  - Manuais (codificação com scripts ou SQL)
  - Workflows
  - Mistas

### Tarefas

- Qualidade de Dados:
  - Correto, Não ambíguo, Consistente, Completo
- Limpar (duplicados, regras de negócio, etc)
- Alteração de codificação (EDCDIC para ASCII)
- Transformar para o modelo dimensional

### Staging

- Armazenamento intermediário dos dados:
  - Após Extração
  - Antes de Transformar e Carregar
- Pode ser processada em memória ou em disco
- Alguns projetos guardam dados de Staging, outros o apagam depois da carag

- Dados não devem ser acessadas por usuários

## Resumo

- Inicialmente, empresas tinham sistemas transacionais
- Armazéns de dados dimensionais foram construídos posteriormente, a partir de modelos já existentes

- Técnica
  - Relações n~n são modeladas em fatos
  - Relações 1~n são modeladas em dimensões
- Negócio
  - Processos de negócio
  - Grão
