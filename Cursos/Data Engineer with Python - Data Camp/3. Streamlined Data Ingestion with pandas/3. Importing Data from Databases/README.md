# Importing Data from Databases

## Introduction to databases

### Relational Databases

- Data about entities is organized into tables
- Each row or record is an instance of an entity
- Each column has information about an attribute
- Tables can be linked to each other via unique keys
- Support more data, multiple simultaneous users, and data quality controls
- Data types are specified for each column
- SQL (Structured Query Language) to interact with databases

### Common Relational Databases

- Microsoft SQL server
- Oracle
- PostgreSQL
- SQLite

- SQLite databases are computer files

### Connecting to Databases

- Two-step process:
  1. Create way to connect to databases
  2. Query database

### Creating a database engine

- `sqlalchemy`s `create_engine()` makes an engine to handle database connections
  - Needs string URL of database to connect to
  - SQLite URL format: `sqlite:///filename.db` (são 3 '\' mesmo)

### Querying databases

- `pd.read_sql(query, engine)` to load in data from a database;
- Arguments:
  - query: String containing SQL query to run or table to load
  - engine: Connection/database engine object.

### SQL Review: SELECT

- Used to query data from a database

- Basic syntax:
```sql
SELECT [column_names] FROM [table_name];
```

- To get all data in a table:
```sql
SELECT * FROM [table_name];
```

- Code style: keywords in ALL CAPS, semicolon (;) to end a statement.

## Refining imports with SQL queries

### WHERE Clauses

- Use a `WHERE` clause to selectively import records

```sql
SELECT [column_names]
FROM [table_name]
WHERE [condition]
```

#### Filtering by numbers

- Compare numbers with mathematical operators
  - =
  - > and >= 
  - < and <=
  - <> (not equal to)

#### Filtering text

- Match exact strings with the = sign and the text to match;
- String matching is case-sensitive

#### Combining conditions: AND

- WHERE clauses with AND return records that meet all conditions

#### Combining conditions: OR

- WHERE clauses with OR return records that meet at least one condition

## More complex SQL queries

### Getting DISTINCT values

- Get unique values for one or more columns with SELECT DISTINCT

```sql
SELECT DISTINCT [column_names] FROM [table_name]
```

### Aggregate Functions

- Query a database directly for descriptive statistics
- Aggregate functions
  - SUM
  - AVG
  - MAX
  - MIN
  - COUNT

- SUM, AVG, MAX, MIN
  - Each takes a single column name
  - `SELECT AVG(tmax) FROM weather;`
- COUNT
  - Get number of rows that meet query conditions
  - `SELECT COUNT(*) FROM [table_name];`
  - - Get number of unique values in a column
  - `SELECT COUNT(DISTINCT [column_names]) FROM [table_name];`

### GROUP BY

- Aggregate functions calculate a single summary statistic by default
- Summarize data by categoriess with `GROUP BY` statements
- Remember to also select the column you're grouping by
