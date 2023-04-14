# Aggregate Functions

## Summarizing data

### Summarizing data

- Aggregate functions return a single value

### Aggregate functions

`AVG()`, `SUM()`, `MIN()`, `MAX()`, `COUNT()`

```
SELECT AVG(budget)
FROM films;
```

### Non-numerical data

Numerical fields only

- AVG()
- SUM()

Various data types

- COUNT()
- MIN()
- MAX()

MIN() <-> MAX()

Minimum <-> Maximum
Lowest <-> Highest
A <-> Z

### Aliasing when summarizing

```SQL
SELECT MIN(country) AS min_country
FROM films;
```

## Summarizing subsets

### Using WHERE with aggregate functions

```SQL
SELECT AVG(budget) AS avg_budget
FROM films
WHERE release_year >= 2010;
```

### ROUND()

- Round a number to a specified decimal

`ROUND(number_to_round, decimal_places)`

### ROUND() using a negative parameter

```SQL
SELECT ROUND(AVG(BUDGET), -5) AS avg_budget
FROM films
WHERE release_year >= 2010;
```

## Aliasing and arithmetic

### Arithmetic

- `SELECT (4 + 3);`
- `SELECT (4 * 3);`
- `SELECT (4 - 3);`
- `SELECT (4 / 3);`
- `SELECT (4.0 / 3.0);`

### Aggregate functions vs. arithmetic

- Aggregate functions works horizontally;
- Arithmetic works vertically;

### Aliasing with arithmetic

```SQL
SELECT (gross - budget) AS profit
FROM films;
```

### Aliasing with functions

```SQL
SELECT MAX(budget) AS max_budget, MAX(duration) AS max_duration
FROM films;
```

### Order of execution

1. FROM
2. WHERE
3. SELECT (aliases are defined here)
4. LIMIT

- Aliases defined in the `SELECT` clause cannot be used in the `WHERE` clause due to order of executions
