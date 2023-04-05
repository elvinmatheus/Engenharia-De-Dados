# Orientado a Documento

## MongoDB

- Open source
- Multiplataforma
- Escalável
- Orientado a documentos: JSON
- Permite documentos aninhados
- Indexados: pode-se buscar o conteúdo dos documentos
- Não tem schema fixo
- Não tem integridade referencial

### Estrutura

| Relacional | MongoDB |
| ---------- | ------- |
| Banco de Dados | Banco de Dados |
| Tabela | Coleção |
| Linha | Documento |
| Coluna | Campo |

### Principais Tipos de Dados

- String
- Inteiro
- Booleano
- Double
- Array
- Timestamp
- Object

### Mais características

- Sem integridade referencial
- Integridade referencial mais flexível
- Pode-se incluir um link para outro documento, porém
  - Não mantém qualquer tipo de integridade
  - Se o outro documento for excluído, o link aponta para "nada"
- Se precisar de integridade referencial, procurar SGBDs que ofereçam suporte a documentos (JSON) com Integridade Referencial.
