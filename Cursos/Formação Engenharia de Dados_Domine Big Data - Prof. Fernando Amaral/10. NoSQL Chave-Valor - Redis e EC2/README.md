# Modelo Chave-Valor

## Redis

- REmote DIctionay Server
- Banco de Dados Chave-valor em memória
- Rápido
- Suporte a vários tipos de dados
- Banco de Dados em memória
- Pode usar disco para persistência

### Aplicações

- Cache de Sessões
  - E-commerce com milhares de usuários
  - A sessão armazena o carrinho de compras

- Cache de páginas
  - Páginas mais acessadas podem ser armazenadas em memória
  - Não é preciso renderizar a página a cada nova requisição

### Banco de Dados

- Não existe o conceito de Banco de Dados como em outros gerenciadores
- Existem separações lógicas para valores com mesmas chaves
- Estas separações são numeradas e fixas, chamadas databases
- São persistidos no mesmo arquivo físico
- Para trocar um banco de dados:
  - SELECT 1
- Padrão é zero

### Outras características

- Suporte a partição (divisão de dados entre instâncias)
- Suporte a Streaming
- Suporte a Cluster

### Estruturas de Dados

- String
- Hashes
- Lists
- Sets
