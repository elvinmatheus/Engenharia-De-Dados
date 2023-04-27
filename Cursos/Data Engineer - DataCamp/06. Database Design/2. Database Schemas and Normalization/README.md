# Database Schemas and Normalization

## Star and snowflake schema

### Star schema

**Dimensional modeling: star schema**

**Fact tables**

- Holds records of a metric
- Changes regularly
- Connects to dimensions via foreign keys

**Dimension tables**

- Holds descriptions of attributes
- Does not change as often

**Example:**

- Supply books to stores in USA and Canada
- Keep track of book sales

### Snowflake schema (an extension)

**Star schemas:** one dimension

**Snowflake schemas:** more than one dimension

Because dimension tables are normalized

### What is normalization?

- Database design technique
- Divides tables into smaller tables and connects them via relationships
- Goal: reduce redundancy and increase data integrity

Identify repeating groups of data and create new tables for them

## Normalized and denormalized databases

Denormalized: star schema

Normalized: snowflake schema

### Denormalized query

Goal> get quantity of all Octavia E. Butler books sold in Vancouver in Q4 of 2018

```SQL
SELECT SUM(quantity) FROM fact_booksales
-- Join to get city
INNER JOIN dim_store_star on fact_booksales.store_id = dim_store_star.store_id
-- Join to get author
INNER JOIN dim_book_star on fact_booksales.book_id = dim_book_star.book_id
-- Join to get year and quarter
INNER JOIN dim_time_star on fact_booksales.time_id = dim_time_star.time_id
WHERE
dim_store_star.city = 'Vancouver' AND dim_book_star.author = 'Octavia E. Butler' AND dim_time_star.year = 2018 AND dim_time_star.quarter = 4;
```

### Normalized query

```sql
SELECT SUM(fact_booksales.quantity) FROM fact_booksales 
-- Join to get city 
INNER JOIN dim_store_sf ON fact_booksales.store_id = dim_store_sf.store_id 
INNER JOIN dim _ city ON dim_store_sf.city_id = dim_city_sf.city_id 
-- Join to get author 
INNER JOIN dim_book_sf ON fact_booksales.book_id = dim_book_sf.book_id 
INNER JOIN dim_author_sf ON dim_book_sf.author_id = dim_author_sf.author_id 
-- Join to get year and quarter 
INNER JOIN dim_time_sf ON fact_booksales.time_id = dim_time_sf.time_id 
INNER JOIN dim_month_sf ON dim_time_sf.month_id = dim_month_sf.month_id 
INNER JOIN dim_quarter_sf ON dim_month_sf.quarter_id = dim_quarter_sf.quarter_id 
INNER JOIN dim_year_sf ON dim_quarter_sf.year_id = dim_year_sf.year_id 
WHERE dim_city_sf.city = `Vancouver` 
AND dim_author_sf.author = `Octavia E. Butler` 
AND dim_year_sf.year = 2018 
AND dim_quarter_sf.quarter = 4;
```

Why would we want to normalize a database?

- Normalization saves space
  - Denormalized databases enable data redundancy
  - Normalization eliminates data redundancy
- Normalization ensures better data integrity
  1. Enforces data consistency: must respect naming conventions because of referential integrity, e.g., 'California', not 'CA' or 'california'
  2. Safer updating, removing and inserting: Less data redundancy = less records to alter
  3. Easier to redesign by extending: Smaller tables are easier to extend than larger tables

### Database normalization

Advantages

- Normalizationi eliminates data redundancy: save on storage
- Better data integrity: accurate and consistent data

Disadvantages

- Complex queries require more CPU

### OLTP and OLAP

- OLTP
  - e.g. Operational databases
  - Typically highly normalized
  - Write-intensive
  - Prioritize quicker and safer insertion of data
- OLAP
  - e.g. Data warehouses
  - Typically less normalized
  - Read-intensive
  - Prioritize quicker queries for analytics
  
## Normal forms

### Normalization

Identify repeating groups of data and create new tables for them

A more formal definition:

The goals of normalization are to:

- Be able to characterize the level of redundancy in a relational schema
- Provide mechanisms for transforming schemas in order to remove redundancy

### Normal forms (NF)

Ordered to least to most normalized

- First normal form (1NF)
- Second normal form (2NF)
- Third normal form (3NF)
- Elementary key normal form (EKNF)
- Boyce-Codd normal form (BCNF)
- Fourth normal form (4NF)
- Essential tuple normal form (ETNF)
- Fifth normal form (5NF)
- Domain-key Normal Form (DKNF)
- Sixth normal form (6NF)

#### 1NF rules

- Each record must be unique - no duplicate rows
- Each cell must hold one value

#### 2NF 

- Must satisfy 1NF AND
  - If primary key is one column
    - Then automatically satisfies 2NF 
  - If there is a composite primary key
    - Then each non-key column must be dependent on all the keys

#### 3NF

- Satisfies 2NF
- No transitive dependencies: non-key columns can't depend on other non-key columns

### Data anomalies

_What is risked if we don't normalize enough?_

1. Update anomaly: Data inconsistency caused by data redundancy when updating
2. Insertion anomaly: Unable to add a record due to missing a
3. Deletion anomaly: Deletion of record(s) causes unintentional loss of data

The more normalized the database, the less prone it will be to data anomalies