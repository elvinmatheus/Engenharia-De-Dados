# Filtering Records

## Filtering numbers

### Where

- `WHERE` filtering clause

```SQL
WHERE color = 'green'
```

### WHERE with comparison operators

```SQL
SELECT title
FROM films
WHERE release_year > 1960;
```

### Comparison operators

- > Greater than or after
- < Less than or before
- = Equal to
- >= Greater than or equal to
- <= Less than or equal to
- <> Not equal to

### WHERE with string

- Use single-quotes around strings we want to filter

### Order of execution

1. FROM
2. WHERE
3. SELECT
4. LIMIT

## Multiple criteria

### Multiple criteria

- OR, AND, BETWEEN


#### OR operator

- Use `OR` when you need to satisfy at least one condition

```SQL
SELECT title
FROM films
WHERE release_year = 1994
   OR release_year = 2000;
```

#### AND operator

- Use `AND` if we need to satisfy all criteria

```SQL
SELECT title
FROM films
WHERE release_year > 1994
  AND release_year < 2000;
```

### AND, OR

- Enclose individual clauses in parentheses

```SQL
SELECT title
FROM films
WHERE (release_year = 1994 OR release_year = 1995)
  AND (certification = 'PG' OR certification = 'R');
```

### BETWEEN, AND

```SQL
SELECT title
FROM films
WHERE release_year >= 1994
  AND release_year <= 2000;
```

```SQL
SELECT title
FROM films
WHERE release_year
    BETWEEN 1994 AND 2000;
```

## Filtering text

### Filtering text

- `WHERE` can also filter text

```sql
SELECT title 
FROM films
WHERE country = 'Japan';
```

- Filter a pattern rather than specific text
- `LIKE`
- `NOT LIKE`
- `IN`

#### LIKE

- Used to search for a pattern in a field

% match zero, one, or many characters
_ match a single character

```sql
SELECT name
FROM people
WHERE name LIKE 'Ade%';
```

```sql
SELECT name
FROM people
WHERE name LIKE 'Ev_';
```

##### NOT LIKE

```SQL
SELECT name
FROM people
WHERE name NOT LIKE 'A.%';
```

#### WHERE, IN

```sql
SELECT title 
FROM films
WHERE release_year IN (1920, 1930, 1940); --Funciona como uma sequência de OR
```

```sql
SELECT title 
FROM films
WHERE country IN ('Germany', 'France');
```

## Null values

### Missing values

- `COUNT(field_name) includes only non-missing values
- COUNT(*) includes missing values

`NULL`

- Missing values:
  - Human error
  - Information not available
  - Unknown

### IS NULL

```SQL
SELECT name
FROM people
WHERE bithdate IS NULL;
```

### IS NOT NULL

```SQL
SELECT COUNT(name) AS count_birthdates
FROM people
WHERE birthdate IS NOT NULL;
```

### NULL put simply

- `NULL` values are missing values
- Very common
- Use `IS NULL` or `IS NOT NULL` to:
  - Identify missing values
  - Select missing values
  - Exclude missing values
