# Database views

## Database views

### Database views

> In a database, a view is the result set of a stored query on the data, which the database users can query just as they would in a persistent database collection object (Wikipedia)

**Virtual table that is not part of the physical schema**

- Query, not data, is stored in memory
- Data is aggregated from data in tables
- Can be queried like a regular database table
- No need to retype common queries or alter schemas

### Creating a view (syntax)

```sql
CREATE VIEW view_name AS
SELECT col1, col2
FROM table_name
WHERE condition
```

### Viewing views (in PostgreSQL)

```sql
SELECT * FROM INFORMATION_SCHEMA.views;
```

Includes system views

```sql
SELECT * FROM information_schema.views;
WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
```

### Benefits of views

- Doesn't take up storage
- A form of access control
  - Hide sensitive columns and restrict what user can see
- Masks complexity of queries
  - Useful for highly normalized schemas
  
## Managing views

### Creating more complex views

- Aggregation: `SUM()`, `AVG()`, `MIN()`, `MAX()`, `GROUP BY`, etc
- Joins: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`
- Conditionals: `WHERE`, `HAVING`, `UNIQUE`, `NOT NULL`, `AND`, `OR`, `>`, `<`, etc

### Granting and revoking access to a view

`GRANT privilege(s)` or `REVOKE privilege(s)`

`ON object`

`TO role` or `FROM role`

- Privileges: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, etc
- Objects: table, view, schema, etc
- Roles: a database user or a group of database users

### Granting and revoking example

```sql
GRANT UPDATE ON ratings to PUBLIC;
```

```sql
REVOKE INSERT ON films FROM db_user;
```

### Updating a view

```SQL
UPDATE films SET kind = 'Dramatic' WHERE kind = 'Drama'
```

Not all views are updatable

- View is madeup of one table
- Doesn't use a window or aggregate function

### Inserting into a view

```SQL
INSERT INTO films (code, title, did, date_prod, kind)
    VALUES ('T_601', 'Yojimbo', 106, '1961-06-16', 'Drama')
```

Not all views are insertable

Takeaway: avoid modifying data through views

### Dropping a view

```SQL
DROP VIEW view_name [ CASCADE | RESTRICT ];
```

- `RESTRICT` (default): returns an error if there are objects that depend on the view
- `CASCADE`: drops view and any object that depends on that view

### Redefining a view

```SQL
CREATE OR REPLACE VIEW view_name AS new_query
```

- If a view with `view_name` exists, it is replaced
- `new_query` must generate the same column names, order, and data types as the old query
- The column output may be different
- New columns may be added at the end

**If these criteria can't be met, drop the existing view and create a new one**

### Altering a view

```SQL
ALTER VIEW [ IF EXISTS ] name ALTER [ COLUMN ] column_name SET DEFAULT expression 
ALTER VIEW [ IF EXISTS ] name ALTER [ COLUMN ] column_name DROP DEFAULT 
ALTER VIEW [ IF EXISTS ] name OWNER TO new_owner 
ALTER VIEW [ IF EXISTS ] name RENAME TO new_name ALTER VIEW [ IF EXISTS ] name SET SCHEMA new_schema 
ALTER VIEW [ IF EXISTS ] name SET ( view_option_name [= view_option_value] [, ... ] 
ALTER VIEW [ IF EXISTS ] name RESET ( view_option_name [, ... ] )
```

## Materialized views

### Two types of views

Views

- Also known as non-materialized views

Materialized views

- Physically materialized

### Materialized views

- Stores the query results, not the query
- Querying a materialized view means accessing the stored query results
  - Not running the query like a non-materialized view
- Refreshed or rematerialized when prompted or scheduled

### When to use materialized views

- Long running queries
- Underlying query results don't change often
- Data warehouses because OLAP is not write-intensive
  - Save on computational cost of frequent queries

### Implementing materialized views (in PostgreSQL)

```sql
CREATE MATERIALIZED VIEW my_mv AS SELECT * FROM existing_table;
```

```sql
REFRESH MATERIALIZED VIEW my_mv;
```

### Managing dependencies

- Materialized views often depend on other materialized views
- Creates a dependency chain when refreshing views
- Not the most efficient to refresh all views at the same time

### Tools for managing dependencies

- Use Directed Acyclic Graphs (DAGs) to keep track of views
- Pipeline scheduler tools