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

**Connection string/URI**

```
postgresql://[user[:password]@][host][:port]
```

**Use in Python**

```python
import sqlalchemy
connection_uri = "postgresql://repl:password@localhost:5432/pagila"
db_engine = sqlalchemy.create_engine(connection_uri)

import pandas as pd
pd.read_sql("SELECT * FROM customer", db_engine)
```

## Transform

### Kinds of transformartions

- Selection of attribute;
- Translation of code values; (e.g. 'New York' -> 'NY')
- Data validation;
- Splitting columns into multiple columns;
- Joining from multiple sources.

**An example: split (Pandas)**

```python
customer_df # Pandas DataFrame with customer data

# Split email column into 2 columns on the '@' symbol
split_email = customer_df.email.str.split("@", expand=True)
# At this point, split_email will have 2 columns, a first
# one with everythin before @, and a second one with
# everything after @

# Create 2 new columns using the resulting DataFrame.
customer_df = customer_df.assign(
	username=split_email[0],
	domain=split_email[1]
```

**Extract data into PySpark**

```python
import pyspark.sql

spark = pyspark.sql.SparkSession.builder.getOrCreate()

spark.read.jdbc("jdbc:postgresql://localhost:5432/pagila",
				"customer",
				properties={"user":"repl","password":"password"})
```

**An example: join (PySpark)**

```python
customer_df # PySpark DataFrame with customer data
ratings_df # PySpark DataFrame with ratings data

# Groupby ratings
ratings_per_customer = ratings_df.groupBy("customer_id").mean("rating")

# Join on customer ID
customer_df.join(
	ratings_per_customer,
	customer_df.customer_id==ratings_per_customer.customer_id
)
```

## Load

### MPP Databases

Massively Parallel Processing Databases:

- Often a target at the end of an ETL process;
- Column-oriented;
- Optimized for analytics;
- Queries are not executed on a single compute node, but rather split into substasks and distributed among several nodes;
- Examples: Amazon Redshift, Azure SQL Data Warehouse, or Google BigQuery.

**An example: Redshift**

Load from file to columnar storage format

```python
# Pandas .to_parquet() method
df.to_parquet("./s3://path/to/bucket/customer.parquet")
# PySpark .write.parquet() method

df.write.parquet("./s3://path/to/bucket/customer.parquet")
```

```SQL
COPY customer
FROM 's3://path/to/bucket/customer.parquet'
FORMAT as parquet
...
```

### Load to PostgreSQL

> "In other cases, you might wand to load the result of the transformation phase into a PostgreSQL database."

`pandas.to_sql()`

```python
# Transformation on data
recommendations = transform_find_recommendations(ratings_df)

# Load into PostgreSQL database
recommendations.to_sql("recommendations",
					   db_engine,
					   schema="store",
					   if_exists="replace")
```

## Putting it all together

1. Create functions to extract, transform and load.
2. Create an etl function to encapsulate the ETL behavior.
3. Create an scheduler using Airflow.

```python
def extract_table_to_df(tablename, db_engine):
	return pd.read_sql("SELECT * FROM {}".format(tablename), db_engine)

def split_columns_transform(df, column, pat, suffixes):
	# Converts column into str and splits it on pat...

def load_df_into_dwh(film_df, tablename, schema, db_engine):
	return pd.to_sql(tablename, db_engine, schema=schema, if_exissts="replace")

db_engines = { ... } # Needs to be configured

def etl():
	# Extract
	film_df = extract_table_to_df("film", db_engines["store"])
	# Transform
	film_df =  split_columns_transform(film_df, "rental_rate", ".", ["_dollar", "_cents"])
	# Load
	load_df_into_dwh(film_df, "film", "store", db_engines["dwh"])
```

**Scheduling with DAGs in Airflow**

```python
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

dag = DAG(dag_id="etl_pipeline",
		  schedule_interval="0 0 * * *")

etl_task = PythonOperator(task_id="etl_task",
						  python_callable=etl,
						  dag=dag)

etl_task.set_upstream(wait_for_this_task)
```
