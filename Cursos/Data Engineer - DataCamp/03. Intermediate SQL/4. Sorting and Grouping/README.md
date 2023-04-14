# Sorting and Grouping

## Sorting results

### ORDER BY

```sql
SELECT title, budget
FROM films
ORDER BY budget;
```

#### ASCending

```sql
SELECT title, budget
FROM films
ORDER BY budget ASC;
```

#### DESCending

```SQL
SELECT title, budget
FROM films
ORDER BY budget DESC;
```

### ORDER BY multiple fields

- `ORDER BY field_one, field_two`
- Think of `field_two` as a tie-breaker

```sql
SELECT title, wins, imdb_score
FROM best_movies
ORDER BY wins DESC, imdb_score DESC;
```

### Order of execution

1. FROM
2. WHERE
3. GROUP BY
4. SELECT
5. DISTINCT
6. ORDER BY
7. LIMIT

## Grouping data

### GROUP BY single fields

```SQL
SELECT certification, COUNT(title) AS title_count
FROM films
GROUP BY certification;
```

### GROUP BY multiple fields

```SQL
SELECT certification, language, COUNT(title) AS title_count
FROM films
GROUP BY certification, language;
```

### GROUP BY with ORDER BY 

```SQL
SELECT certification, COUNT(title) as title_count
FROM films
GROUP BY certification
ORDER BY title_count DESC;
```

### Order of execution

1. FROM
2. WHERE
3. GROUP BY
4. SELECT
5. DISTINCT
6. ORDER BY
7. LIMIT

## Filtering grouped data

### HAVING

```SQL
SELECT release_year, COUNT(title) AS title_count
FROM films
GROUP BY release_year
HAVING COUNT(title) > 10;
```

### Order of execution

1. FROM
2. WHERE
3. GROUP BY
4. HAVING 
5. SELECT
6. DISTINCT
7. ORDER BY
8. LIMIT

### HAVING vs WHERE

- WHERE filters individual records, HAVING filters grouped records
