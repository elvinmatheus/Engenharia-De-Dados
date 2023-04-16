# Enforce data consistency with attribute constraints

## Better data quality with constraints

### Integrity constraints

1. Attribute constraints, e.g. data types on columns
2. Key constraints, e.g. primary keys
3. Referential integrity constraints, enforced through foreign keys

### Why constraints?

- Constraints give the data structure
- Constraints help with consistency, and thus data quality
- Data quality is a business advantage / data science prerequisite
- Enforcing is difficult, but PostgreSQL helps

### Data types as attribute constraints

- Check the DBMS's documentation

### Dealing with data types (casting)

```SQL
SELECT temperature * CAST(wind_speed AS integer) AS wind_chill
FROM weather;
```

## Working with data types

### Working with data types

- Enforced on columns (i.e. attributes)
- Define the so-called "domain" of a column
- Define what operations are possible
- Enforce consistent storage of values

### The most common types

- `text` : character strings of any lenght
- `varchar [ (n) ] ` : a maximum of `n` characters
- `char [ (x) ]` : a fixed-length string of `n` characters
- `boolean` : can only take three states, e.g. `TRUE`, `FALSE` and `NULL` (unknown)
- `date`, `time`, `timestamp` : various formats for date and time calculations
- `numeric` : arbitrary precision numbers, e.g. `3.1457`
- `integer` : whole numbers in the range of ...

Check the DBMS's documentation.

### Specifying types upon table creation

```SQL
CREATE TABLE students (
    ssn integer,
    name varchar(64),
    dob date,
    average_grade numeric(3, 2), -- e.g. 5.54
    tuition_paid boolean
);
```

### Alter types after table creation

```SQL
ALTER TABLE students
ALTER COLUMN name
TYPE varchar(128);
```

```SQL
ALTER TABLE students
ALTER COLUMN average_grade
TYPE integer
-- Turns 5.54 into 6, not 5, before type conversion
USING ROUND(average_grade);
```

## The not-null and unique constraints

### The not-null constraint

- Disallow `NULL` values in a certain column
- Must hold true for the current state
- Must hold true for any future state

### What does NULL mean?

- unknown
- does not exist
- does not apply
- ...

```sql
CREATE TABLE students (
    ssn integer not null,
    lastname varchar(64) not null,
    home_phone integer,
    office_phone integer
);
```

### How to add or remove a not-null constraint

When creating a table...

```sql
CREATE TABLE students (
    ssn integer not null,
    lastname varchar(64) not null,
    home_phone integer,
    office_phone integer
);
```

After the table has been created...

```sql
ALTER TABLE students
ALTER COLUMN home_phone
SET NOT NULL;
```

```SQL
ALTER TABLE students
ALTER COLUMN ssn
DROP NOT NULL
```

### The unique constraint

- Disallow duplicate values in a column
- Must hold true for the current state
- Must hold true for any future state

### Adding unique constraints

```sql
CREATE TABLE table_name (
    column_name UNIQUE
);
```

```SQL
ALTER TABLE table_name
ADD CONSTRAINT some_name UNIQUE(column_name)
```