# Database management

## Database roles and access control

### Granting and revoking access to a view

`GRANT privilege(s)` or `REVOKE privilege(s)`

`ON object`

`TO role` or `FROM role`

- Privileges: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, etc.
- Objects: table, view, schema, etc
- Roles: a database user a group of database users

```sql
GRANT UPDATE ON ratings TO PUBLIC;
REVOKE INSERT ON films FROM db_user;
```

### Database roles

- Manage database access permissions
- A database role is an entity that contains information that:
  - Define the role's privileges
    - Can you login?
    - Can you create databases?
    - Can you write to tables?
  - Roles can be assigned to one or more users
  - Roles are global across a database cluster installation

### Create a role

- Empty role

`CREATE ROLE data_analyst;`

- Roles with some attributes set

`CREATE ROLE intern WITH PASSWORD 'PasswordForIntern' VALID UNTIL '2020-01-01';`

`CREATE ROLE admin CREATEDB;`

`ALTER ROLE admin CREATEROLE`

### GRANT and REVOKE privileges from roles

`GRANT UPDATE ON ratings TO data_analyst;`

`REVOKE UPDATE ON ratings FROM data_analyst;`

The available privileges in PostgreSQL are:

- `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`, `REFERENCES`, `TRIGGER`, `CREATE`, `CONNECT`, `TEMPORARY`, `EXECUTE`, and `USAGE`

### Users and groups (are both roles)

- A role is an entity that can function as a user and/or a group
  - User roles
  - Group roles
  
**Group role**

```SQL
CREATE ROLE data_analyst;
```

**User role**

```SQL
CREATE ROLE intern WITH PASSWORD 'PasswordForIntern' VALID UNTIL '2020-01-01';
```

```SQL
CREATE ROLE alex WITH PASSWORD 'PasswordForIntern' VALID UNTIL '2020-01-01';
```

```SQL
GRANT data_analyst TO alex;
```

```SQL
REVOKE data_analyst FROM alex;
```

### Benefits and pitfalls of roles

**Benefits**

- Roles live on after users are deleted
- Roles can be created before user accounts
- Save DBAs time

**Pitfalls**

- Sometimes a role gives a specific user too much access
  - You need to pay attention
  
## Table partitioning

### Why partition?

Tables grow (100s Gb / Tb)

Problem: queries/updates become slower

Because: e.g., indices don't fit memory

Solution: split table into smaller parts (= partitioning)

### Data modeling refresher

1. Conceptual data model
2. Logical data model
  - For partitioning, logical data model is the same
3. Physical data model
  - Partitioning is part of physical data model
  
### Vertical partitioning

- Split table even when fully normalized

### Horizontal partitioning

```sql
CREATE TABLE sales (
    ...
    timestamp DATE NOT NULL
)
PARTITION BY RANGE (timestamp);

CREATE TABLE sales_2019_q1 PARTITION OF sales
    FOR VALUES FROM ('2019-01-01') TO ('2019-03-31')
...
CREATE TABLE sales_2019_q4 PARTITION OF sales
    FOR VALUES FROM ('2019-09-01') TO ('2019-12-31');
CREATE INDEX ON sales ('timestamp');
```

### Pros/cons of horizontal partitioning

Pros

- Indices of heavily-used partitions fit in memory
- Move to specific medium: slower vs. faster
- Used for both OLAP as OLTP

Cons

- Partitioning existing table can be a hassle
- Some constraints can not be set

## Data integration

### What is data integration

Data integration combines data from different sources, formats, technologies to provide users with a translated and unified view of that data

### Business case examples

- 360-degree customer view
- Acquisition
- Legacy systems

### Choosing a data integration tool

- Flexible
- Reliable
- Scalable

## Picking a database management system (DBMS)

### DBMS

- DBMS: DataBase Management System
- Create and maintain databases
  - Data
  - Database schema
  - Database engine
- Interface between database and end users

### DBMS types

- Choice of DBMS depends on database type
- Two types:
  - SQL DBMS
  - NoSQL DBMS

#### SQL DBMS

- Relational DataBase Management System (RDBMS)
- Based on the relational model of data
- Query language: SQL
- Best option when:
  - Data is structured and unchanging
  - Data must be consistent
  
#### NoSQL DBMS 

- Less structured
- Document-centered rather than table-centered
- Data doesn't have to fit into well-defined rows and columns
- Best option when:
  - Rapid growth
  - No clear schema definitions
  - Large quantities of data
- Types: key-value store, document store, columnar database, graph database

##### NoSQL DBMS - key-value store

- Combinations of keys and values
  - Key: unique identifier
  - Value: anything
- Use case: managing the shopping cart for an on-line buyer
- Example: redis

##### NoSQL DBMS - document store

- Similar to key-value
- Values (= documents) are structured
- Use case: content management
- Example: mongoDB

##### NoSQL DBMS - columnar database

- Store data in columns
- Scalable
- Use case: big data analytics where speed is important
- Example: cassandra

##### NoSQL DBMS - graph database

- Data is interconnected and best represented as a graph
- Use case: social media data, recommendations
- Example: neo4j