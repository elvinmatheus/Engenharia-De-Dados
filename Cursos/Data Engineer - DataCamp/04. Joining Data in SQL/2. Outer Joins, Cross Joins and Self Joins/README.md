# Outer Joins, Cross Joins and Self Joins

## LEFT and RIGHT JOINs

### LEFT JOIN initial diagram

- `LEFT JOIN` will return all records in the left table, and those records in the right table that match on the joining field provided.

```SQL
SELECT pm.country, prime_minister, president
FROM prime_ministers AS pm
LEFT JOIN presidents AS p
USING(country);
```

**Note**: `LEFT JOIN` can also be written as `LEFT OUTER JOIN`.

### RIGHT JOIN

```SQL
SELECT * 
FROM left_table
RIGHT JOIN right_table
ON left_table.id = right_table.id;
```

**Note:** `RIGHT JOIN` can also be written as `RIGHT OUTER JOIN`.

### LEFT JOIN or RIGHT JOIN?

- `RIGHT JOIN` is less commonly used than `LEFT JOIN`
- Any `RIGHT JOIN` can be re-written as a `LEFT JOIN`
- `LEFT JOIN` feels more intuitive to users whe typing from left to right

## FULL JOINs

### FULL JOIN initial diagram

- A `FULL JOIN` combines a `LEFT JOIN` and a `RIGHT JOIN`

```SQL
SELECT left_table.id AS L_id,
		right_table.id AS R_id,
		left_table.val AS L_val,
		right_table.val AS R_val
FROM left_table
FULL JOIN right_table
USING(id);
```
**Note:** The keyword `FULL OUTER JOIN` can also be used.

## Crossing into CROSS JOIN

### CROSS JOIN diagram

`CROSS JOIN` creates all possible combinations of two tables.

```SQL
SELECT id1, id2
FROM table1
CROSS JOIN table2;
```

## Self joins

### Self joins

- Self joins are tables joined with themselves
- They can be used to compare parts of the same table
