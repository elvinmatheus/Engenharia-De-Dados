# Processing, Storing, and Organizing Data

## OLTP and OLAP

### How should we organize and manage data?

- Schemas: How should my data be logically organized?
- Normalization: Shoul my data have minimal dependency and redundancy
- Views: What joins will be done most often?
- Access control: Should all users of the data have the same level of access
- DMBS: How do I pick between all the SQL and noSQL options?

It depends on the intended use of the data.

### Approaches to processing data

- OLTP: Online Transaction Processing
- OLAP: Online Analytical Processing

### Some concrete examples

- OLTP tasks
  - Find the price of a book
  - Update latest customer transaction
  - Keep track of emplyee hours
  
- OLAP tasks
  - Calculate books with best profit margin
  - Find most loyal customers
  - Decide employee of the month
 
### OLAP VS OLTP

|         | OLTP                                   | OLAP                                         |
|---------|----------------------------------------|----------------------------------------------|
| Purpose | support daily transactions             | report and analyze data                      |
| Design  | application-oriented                   | subject-oriented                             |
| Data    | up-to-date, operational                | consolidated, historical                     |
| Size    | snapshot, gigabytes                    | archive, terabytes                           |
| Queries | simple transactions & frequent updates | complex, aggregate queries & limited updates |
| Users   | thousands                              | hundreds                                     |

They work together

## Storing data

1. Structured data
  - Follows a schema
  - Defined data types and relationships
  - e.g., SQL, tables in a relational database
 
2. Unstructured data
  - Schemaless
  - Makes up most of data in the world
  - e.g. photos, chat logs, MP3

3. Semi-structured data
  - Does not follow larger schema
  - Self-describing structure
  - e.g. NoSQL, XML, JSON
  
More structured = Easier to analyze
Less structured = More flexibility and Scalability

### Storing data beyond traditional databases

- Traditional databases
  - For storing real-time relational structured data? OLTP
- Data warehouses
  - For analyzing archived structured data? OLAP
- Data lakes
  - For storing of all structures = flexibility and scalability
  - For analyzing big data
  
### Data warehouses

- Optimized for analytics - OLAP
  - Organized for reading/aggregating data
  - Usually read-only
- Contains data from multiple sources
- Massively Parallel Processing (MPP)
- Typically uses a denormalized schema and dimensional modelling

#### Data marts

- Subset of data warehouses
- Dedicated to a specific topic

### Data lakes

- Store all types of data at a lower cost:
  - e.g., raw, operational databases, IoT device logs, real-time, relational and non-relational
- Retains all data and can take up petabytes
- Schema-on-read as opposed to schema-on-write
- Need to catalog data otherwise becomes a data swamp
- Run big data analytics using services such as Apache Spark and Hadoop
  - Useful for deep learning and data discovery because activities require so much data
  
### ETL e ELT

## Database design

### What is database design?

- Determines how data is logically stored
  - How is data going to be read and updated?
- Uses database models: high-level specifications for database structure
  - Most popular: relational model
  - Some other options: NoSQL models, object-oriented model, network model
- Uses schemas: blueprint of the database
  - Defines tables, fields, relationships, indexes, and views
  - When inserting data in relational databases, schemas must be respected
  
### Data modelling

Process of creating a data model for the data to be stored

1. Conceptual data model: descirbes entities, relationships, and attributes
  - Tools: data structure diagrams, e.g. entity-relational diagrams and UML diagrams
2. Logical data model: defines tables, columns, relationships
  - Tools: database models and schemas, e.g., relational model and star schema
3. Physical data model: describes physical storage
  - Tools: partitions, CPUs, indexes, backup systems and tablespaces
  
Entities (conceptual) become the tables (logical)

### Beyond the relational model

**Dimensional modeling**

Adaptation of the relational model for data warehouse design

- Optimized for OLAP queries: aggregate data, not updating (OLTP)
- Built using the star schema
- Easy to interpret and extend schema

### Elements of dimensional modeling

**Organize by:**

- What is being analyzed?
- How often do entities change?

**Fact tables**

- Decided by business use-case
- Holds records of a metric
- Changes regularly
- Connects to dimensions via foreign keys

**Dimension tables**

- Holds descriptions of attributes
- Does not change as often