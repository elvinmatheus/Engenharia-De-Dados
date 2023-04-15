# Subqueries

## Subquerying with semi joins and anti joins

### Semi join

A **semi join** chooses records in the first table where a condition is met in the second table.

### Anti join

Return all values from left_table where col1 values are **not** in col2

## Subqueries inside WHERE and SELECT

### Syntax for subqueries inside WHERE

- All semi joins and anti joins include a subquery in `WHERE`
- `WHERE` is the most common place for subqueries

```SQL
SELECT * 
FROM some_table
WHERE some_numeric_field IN (include subquery here);
```

### Subqueries inside SELECT

```SQL
SELECT DISTINCT continent,
	(SELECT COUNT(*)
	 FROM monarchs
	 WHERE states.continent = monarchs.continent) AS monarch_count
FROM states;
```

## Subqueries inside FROM

### Subqueries inside FROM

```SQL
SELECT DISTINCT monarchs.continent, sub.most_recent
FROM monarchs,
	(SELECT
		continent,
		MAX(indep_year) AS most_recent
	 FROM states
	 GROUP BY continent) AS sub
WHERE monarchs.continent = sub.continent
ORDER BY continent;
```
