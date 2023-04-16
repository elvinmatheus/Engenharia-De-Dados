# Uniquely identify records with key constraints

## Keys and superkeys

### What is a key?

- Attribute(s) that identify a record uniquely
- As long as attributes can be removed: superkey
- If no more attributes can be removed: minimal superkey or key

## Primary keys

### Primary keys

- One primary key per database table, chosen from candidate keys
- Uniquely identifies records, e.g. for referencing in other tables
- Unique and not-null constraints both apply
- Primary keys are time-invariant

### Specifying primary keys

```sql
CREATE TABLE products (
    product_no integer UNIQUE NOT NULL, 
    name text,
    price numeric
);
CREATE TABLE products (
    product_no integer PRIMARY KEY,
    name text,
    price numeric
);
```

```SQL
CREATE TABLE example (
    a integer,
    b integer,
    c integer,
    PRIMARY KEY (a, c)
);
```

```SQL
ALTER TABLE table_name
ADD CONSTRAINT some_name PRIMARY KEY (column_name);
```

## Surrogate keys

### Surrogate keys

- Primary keys should be built from as few columns as possible
- Primary keys should never change over time

### Adding a surrogate key with serial data type

```SQL
ALTER TABLE cars
ADD COLUMN id serial PRIMARY KEY;
INSERT INTO cars
VALUES('Volkswagen', 'Blitz', 'black');
```

### Another type of surrogate key

```SQL
ALTER TABLE table_name
ADD COLUMN column_c varchar(256);

UPDATE table_name
SET column_c = CONCAT(column_a, column_b)
ALTER TABLE table_name
ADD CONSTRAINT pk PRIMARY KEY (column_c)
```