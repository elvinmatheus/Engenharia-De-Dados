# Selecting Data

## Querying a database

### COUNT()

- `COUNT()`
- Counts the number of records with a value in a field
- Use an alias for clarity

```SQL
SELECT COUNT(birthdate) AS count_birthdates
FROM people;
```

#### COUNT() multiple fields

```SQL
SELECT COUNT(name) AS count_names, COUNT(birthdate) AS count_birthdates
FROM people;
```

#### Using * with COUNT()

- `COUNT(field_name) counts values in a field
- `COUNT(*)` counts records in a table
- * represents all fields

```SQL
SELECT COUNT(*) AS total_records
FROM people;
```

### DISTINCT

- `DISTINCT` removes duplicates to return only unique values

```SQL
SELECT DISTINCT language
FROM films;
```

### COUNT() with DISTINCT

- Combine `COUNT()` with `DISTINCT` to count unique values

```SQL
SELECT COUNT(DISTINCT birthdate) AS count_distinct_birthdates
FROM people;
```

- `COUNT()` includes duplicates
- `DISTINCT` excludes duplicates

## Query execution

### Order of execution

- SQL is not processed in its written order

```SQL
SELECT name
FROM people
LIMIT 10;
```

Logical order: 

1. FROM
2. SELECT
3. LIMIT

- `LIMIT` limits how many results we return
- Good to know processing order for debugging and aliasing
- Aliases are declared in the SELECT statement

### Debugging SQL

- Mispelling (keyword errors)
- Incorrect capitalization
- Incorrect or missing punctuation (comma errors)

## SQL style

### SQL formatting 

- Formatting is not required
- But lack of formatting can cause issues

```SQL
select title, release_year, country from films limit 3
```

### Best practices

- Capitalize keywords
- Add new lines

```SQL
SELECT title, release_year, country
FROM films
LIMIT 3;
```

### Style guides

- Holyweell's style guide: [https://www.sqlstyle.guide/](https://www.sqlstyle.guide/)

### Semicolon

- Best practice
- Easier to translate between SQL flavors
- Indicates the end of a query

```SQL
SELECT title, release_year, country
FROM films
LIMIT 3;
```

### Dealing with non-standard field names

- `release year` instead of `release_year`
- Put non-standard field names in double-quotes

```SQL
SELECT title, "release year", country
FROM films
LIMIT 3;
```

### Why do we format?

- Easier collaboration
- Clean and readable
- Looks professional
- Easier to understand
- Easier to debug
