# Extract, Transform and Load (ETL)

## Extract

> "Means extracting data from persistent storage, which is not suited for data processing, into memory. Persistent storage could be a file on Amazon S3, for example, or a SQL database. The sources to extract from vary."

### Extract from text files

> "We can extract data from plain text files. They can be unstructured, like a chapter of a book. Alternatively, these can be flat files, where each row is a record, and each column is an attribute of the records. Typical examples of flat files are comma-, or tab-separated files: .csv or .tsv."

#### JSON

> "Another widespread data format is called JSON, or JavaScript Object Notation. JSON files hold information in a semi-structured way. It consists of 4 atomic data types: number, string, boolean and null. There are also 2 composite data types: array and object."

#### Data on the Web through APIs

Web servers that serve that in a JSON data format.

> "We call these servers APIs or Application Programming Interfaces."

### Data in databases

> "The most common way of data extraction is extraction from existing application databases. Most applications, like web services, need a database to back them up and persist data."

#### OLTP

> "Databases that applications like web services use, are typically optimized for having lots of transactions. A transaction typically changes or interts rows, or records in the database. These kinds of transactional databases are called OLTP, or Online Transaction Processing. They are typically row-oriented, in which the systems adds data per rows."

#### OLAP

> "In contrast, databases optimized for analysis are called OLAP, or Online Analytical Processing. They are often column-oriented."

#### Extraction from databases

> "To extract data from a database in Python, you'll always need a connection string."

## Transform

### Kinds of transformartions

- Selection of attribute;
- Translation of code values; (e.g. 'New York' -> 'NY')
- Data validation;
- Splitting columns into multiple columns;
- Joining from multiple sources.

## Load

### MPP Databases

Massively Parallel Processing Databases:

- Often a target at the end of an ETL process;
- Column-oriented;
- Optimized for analytics;
- Queries are not executed on a single compute node, but rather split into substasks and distributed among several nodes;
- Examples: Amazon Redshift, Azure SQL Data Warehouse, or Google BigQuery.

### Load to PostgreSQL

> "In other cases, you might wand to load the result of the transformation phase into a PostgreSQL database."

## Putting it all together

1. Create functions to extract, transform and load.
2. Create an etl function to encapsulate the ETL behavior.
3. Create an scheduler using Airflow.
