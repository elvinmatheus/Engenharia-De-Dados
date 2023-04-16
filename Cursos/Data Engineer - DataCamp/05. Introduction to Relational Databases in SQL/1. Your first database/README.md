# Your first database

## Your first database

### A relational database:

- real-life _entities_ become _tables_ (e.g. `professors`, `universities`, `companies`)
- reduced redundancy (e.g. only one entry in `companies` for the bank "Credit Suisse")
- data integrity by _relationships_ (e.g. a `professor` can work at multiple `universities` and `companies`, a `company` can employ multiple `professors`)

### Have a look at the PostgreSQL database

```SQL
SELECT table_schema, table_name
FROM information_schema.tables;
```

## Tables: At the core of every database

### Create new tables with CREATE TABLE

```SQL
CREATE TABLE table_name (
	column_a data_type,
	column_b data_type,
	column_c data_type
);
```

## Update your database as the structure changes

### The INSERT INTO statement

```SQL
INSERT INTO table_name (column_a, column_b)
VALUES ("value_a", "value_b")
```

### RENAME a COLUMN

```sql
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;
```

### DROP a COLUMN in affiliations

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```
