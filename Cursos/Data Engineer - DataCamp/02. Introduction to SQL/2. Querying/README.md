# Querying

## Introducing queries

### What is SQL useful for?

- Best for large datasets

### Keywords

_Keywords_ are reserved words for operations

Common keywords: `SELECT`, `FROM`

```SQL
SELECT name
FROM patrons;
```

- Query results often called result set

### Selecting multiple fields

```SQL
SELECT name, card_num, total_fine
FROM patrons;
```

### Selecting all fields

```SQL
SELECT *
FROM patrons;
```

## Writing queries

### Aliasing

Use _aliasing_ to rename columns

```SQL
SELECT name AS first_name, year_hired
FROM employees;
```

### Selecting distinct records

```SQL
SELECT DISTINCT dept_id, year_hired
FROM employees;
```

### Views

- A _view_ is a virtual table that is the result of a saved SQL `SELECT` statement
- When accessed, views automatically update in response to updates in the underlying data

```SQL
CREATE VIEW employee_hire_years AS
SELECT id, name, year_hired
FROM employees;
```

### Using views

```SQL
SELECT id, name
FROM employee_hire_years;
```

## SQL flavors

### SQL flavors

- Both free and paid
- All used with relational databases
- Vast majority of keywords are the same
- All must follow universal standards
- Only the additions on top of these standards make flavors different

### Two popular SQL flavors

#### PostgreSQL

- Free and open-source relational database system
- Created at the University of California, Berkeley
- "PostgreSQL" refers to both the PostgreSQL database system and its associated SQL flavor

#### SQL server

- Has free and paid versions
- Created by Microsoft
- T-SQL is Microsoft's SQL flavor, used with SQL Server databases

#### Comparison

- Like dialects of the same language
- Example: limiting number of results

PostgreSQL:

```SQL
SELECT id, name
FROM employees
LIMIT 2;
```

SQL Server:

```SQL
SELECT id, name
FROM employees
TOP 2;
```
