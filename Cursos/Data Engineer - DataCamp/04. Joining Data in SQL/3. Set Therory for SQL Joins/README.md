# Set Theory for SQL Joins

## Set theory for SQL Joins

### UNION diagram

- `UNION` takes two tables as input, and returns all records from both tables

```SQL
SELECT *
FROM left_table
UNION
SELECT *
FROM right_table;
```

### UNION ALL diagram

- `UNION ALL` takes two tables and returns all records from both tables, including duplicates

```SQL
SELECT *
FROM left_table
UNION ALL
SELECT *
FROM right_table;
```

## At the INTERSECT

### INTERSECT syntax

```SQL
SELECT id, val
FROM left_tale
INTERSECT
SELECT id, val
FROM right_table;
```

Exibe somente os registros que as duas consultas têm em comum.

## EXCEPT

### EXCEPT syntax

```SQL
SELECT monarch, country
FROM monarchs
EXCEPT
SELECT prime_minister, country
FROM prime_ministers;
```

Exibe somente os registros da tabela A que não são iguais aos da tabela B.
