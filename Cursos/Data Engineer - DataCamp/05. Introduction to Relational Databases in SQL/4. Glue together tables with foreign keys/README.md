# Glue together tables with foreign keys

## Model 1:N relationships with foreign keys


### Implementing relationships with foreign keys

- A foreign key (FK) points to the primary key (PK) of another table
- Domain of FK must be equal to domain of PK
- Each value of FK must exist in PK of the other table (FK constraint or "referential integrity")
- FKs are not actual keys


### Specifying foreign keys

```SQL
CREATE TABLE manufacturers (
    name varchar(255) PRIMARY KEY);
    
INSERT INTO manufacturers
VALUES ('Ford'), ('VW'), ('GM');

CREATE TABLE cars (
    model varchar(255) PRIMARY KEY,
    manufacturer_name varchar(255) REFERENCES manufacturers (name));
    
INSERT INTO cars
VALUES ('Ranger', 'Ford'), ('Beetle', 'VW');
```

```SQL
INSERT INTO cars
VALUES ('Tundra', 'Toyota');
```

### Specifying foreign keys to existing tables

```sql
ALTER TABLE a
ADD CONSTRAINT a_fkey FOREIGN KEY (b_id) REFERENCES b (id);
```

## Model more complex relationships

### How to implement N:M-relationships

- Create a table
- Add foreign keys for every connected table 
- Add additional attributes

```sql
CREATE TABLE affiliations (
    professor_id integer REFERENCES professors (id),
    organization_id varchar(256) REFERENCES organizations (id),
    function varchar(256))
```

- No primary key
- Possible PK = {professor_id, organization_id, function}

## Referential integrity

### Referential integrity

- A record referencing another table must refer to an existing record in that table
- Specified between two tables
- Enforced through foreign keys

### Referential integrity violations

Referential integrity from table A to table B is violated...

- ... if a record in table B that is referenced from a record in table A is deleted.
- ... if a record in table A referencing a non-existing from table B is inserted.
- Foreign keys prevent violations

### Dealing with violations

```sql
CREATE TABLE a (
    id integer PRIMARY KEY, 
    column_a varchar(64),
    ...,
    b_id integer REFERENCES b (id) ON DELETE NO ACTION
)
```

ON DELETE...

- ...NO ACTION: Throw an error
- ...CASCADE: Delete all referencing records
- ...RESTRICT: Throw an error
- ...SET NULL: Set the referencing column to NULL
- ...SET DEFAULT: SET the referencing column to its default value