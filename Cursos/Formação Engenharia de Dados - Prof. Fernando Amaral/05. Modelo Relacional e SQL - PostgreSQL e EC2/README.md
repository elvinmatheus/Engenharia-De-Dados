# Modelo Relacional e SQL

## SQL

- Structured Query Language, ou Linguagem de Consulta Estruturada

- DQL - Linguagem de Consulta de Dados
  - SELECT
- DML - Linguagem de Manipulação de Dados
  - INSERT, UPDATE, DELETE
- DDL - Linguagem de Definição de Dados
  - CREATE TABLE, INDEX, VIEW
  - ALTER TABLE, INDEX, VIEW
- DCL - Linguagem de Transação de Dados
  - GRANT, REVOKE
- DTL - Linguagem de Transação de Dados
  - BEGIN TRANSACTION, COMMIT, ROLLBACK

### JOINS

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN

## Modelo Relacional

-  Proposto pelo matemático Edgar Frank Codd em 1970, sendo descrito no artigo "Relational Model of Data for Large Shared Data Banks"
- Sucessor do modelo hierárquico e do modelo em rede

- Bom para:
  - Suporte a grande volume de transações (operações)
    - Incluir, excluir, alterar, consultar
  - Rápido
  - Manter Integridade
  - Reduzir redundância
  - Acesso Concorrente

- Não tão bom para:
  - Análise
  - Escalabilidade
  - Redundância

- Responsável por suportar o negócio
  - Mantém a companhia operando

### ACID

- Atomicity, Consistency, Isolation, Durability

#### Atomicity

- Tudo ou nada, se um conjunto de processos falhar (transações) nenhuma delas deverá ter sucesso e o banco de dados não é alterado

#### Consistency

- As mudanças de estado do banco de dados seguem as regras de consistência

#### Isolation

- Os resulstados das transações executadas serão mantidas, mesmo que haja uma transação concorrente

#### Durability

- Se a transação foi concluída com sucesso, seus efeitos permanecerão, mesmo se ocorrerem falhas (rede, energia, hardware, etc.)

### Níveis de isolamento (Isolation Levels)

#### Dirty Read

- Permite a leitura de um registro sem commit

#### Non Repeatable Read

- Transação lê mesmos dados duas vezes, e obtém valores diferentes

#### Phantom read

- Mesma consulta retorna registros diferentes

#### Read uncommited

- Consegue ler registros sendo alterados, mesmo sem commit/rollback
- Não gera bloqueios
- Leitura Suja

#### Read Commited

- Consegue-se ler registros apenas permanentes, commit
- Gera bloqueios
- Não ocorre leitura suja

#### Repeatable Read

- Mais restritivo
- Bloqueia registros e referências para update
- Evita Non-Repeatable read

#### Serializable

- Nível de isolamento mais alto
- Gera lock também em Insert
