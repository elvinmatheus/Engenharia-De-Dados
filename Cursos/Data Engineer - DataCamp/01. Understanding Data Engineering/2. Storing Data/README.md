# Storing data

## Structured data

- Easy to search and organize;
- Consistent model, rows and columns;
- Defined types;
- Can be grouped to form relations;
- Stored in relational databases;
- About 20% of the data is structured;
- Created and queried using SQL.

## Semi-structured data

- Relatively easy to search and organize;
- Consistent model, less-rigid implementation: different observations have different sizes;
- Different types;
- Can be grouped, but needs more work;
- NoSQL databases: JSON, XML, YAML.

## Unstructured data

- Does not follow a model, can't be contained in rows and columns;
- Difficult to search and organize;
- Usually text, sound, pictures or videos;
- Usually stored in data lakes, can appear in data warehouses or databases;
- Most of the data is unstructured;
- Can be extremely valuable.

### Adding some structure

- Use AI to search and organize unstructured data;
- Add information to make it sem-structured.

## SQL

- Structured Query Language;
- Industry standard for Relational Database Management System (RDBMS);
- Allows you to access many records at once, and grouped, filter or aggregate them;
- Close to written English, easy to write and understand;
- Data engineers use SQL to create and maintain databases;
- Data scientists use SQL to query (request information from) databases.

## Database schema

- Databases are made of tables;
- The database schema governs how tables are related.

## Data warehouses and data lakes

- Data lake
  - Stores all the raw data;
  - Can be petabytes;
  - Stores all data structures;
  - Cost-effective;
  - Difficult to analyze;
  - Requires an up-to-date data catalog;
  - Used by data scientists;
  - Big data, real-time analytics.

- Data warehouse
  - Specific data for specific use;
  - Relatively small;
  - Stores mainly structured data;
  - More costly to update;
  - Optimized for data analysis;
  - Also used by data analysts and business analysts;
  - Ad-hoc, read-only queries.

## Data catalog for data lakes

A data catalog is a source of truth that compensates for the lack of structure in a data lake. It responds:

- What is the source of this data?
- Where is this data used?
- Who is the owner of the data?
- How often is this data updated?

Advantages: 

- Good practice in terms of data governance.
- Ensures reproducibility
- No catalog --> data swamp

- It is a good practice for any data storage solution
  - Realibility;
  - Autonomy;
  - Scalability;
  - Speed.

## Databases vs Data warehouses

- Database:
  - General term;
  - Loosely defined as *organized data stored* and *accessed* on a computer;
- Data Warehouse is a type of database.
