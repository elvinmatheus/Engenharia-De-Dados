# Introducing Inner Joins

## The ins and outs of INNER JOIN

### The ins and outs of INNER JOINs

- `INNER JOIN` looks for records in both tables which match on a given field

```SQL
SELECT om.country, pm.continent, prime_minister, president
FROM prime_minister AS pm
INNER JOIN presidents AS p
ON pm.country = p.country
```

**Note**: The `table.column_name` format must be used when selecting columns that exist in both tables to avoid a SQL error.

Aliases can be used in the `table.column_name` syntax in `SELECT` and `ON` clauses

### Using USING

```SQL
SELECT ...
FROM prime_ministers AS pm
INNER JOIN presidents AS p
USING(country)
```

Use USING when the two collumns_names are the same.

## Multiple joins

### Joins on joins

````SQL
SELECT *
FROM left_table
INNER JOIN right_table
ON left_table.id = right_table.id
INNER JOIN another_table
ON left_table.id = another_table.id;
```

**Note**: Depending on the use case, `left_table` or `right_table` can be used in the `ON` clause.
