# Data engineering toolbox

## Databases

> A usually large collection of data organized especially for rapid search and retrieval.

- Holds data;
- Organizes data;
- Retrieve/Search data through DBMS.

### Databases and file storage

- Databases
  - Very organized;
  - Functionality like search, replication, ....
- File systems
  - Less organized;
  - Simple, less added functionality.

### Structured and unstructured data

**Structured**: database schema
- Relational database;

**Semi-structured**
- JSON;

**Unstructured**: schemaless, more like files
- Videos, photos

### SQL and NoSQL

- SQL:
  - Tables;
  - Database schema;
  - Relational databases.

- NoSQL
  - Non-relational databases;
  - Structured or unstructured;
  - Key-value stores (e.g. caching);
  - Document DB (e.g. JSON objects).

### SQL: Star schema

> The star schema consists of one or more fact tables referencing any number of dimension tables.

- **Facts**: things that happened (e.g. Product Orders)
- **Dimensions**: information on the world (e.g. Customer Information)

## What is parallel computing

### Idea behind parallel computing

*Basis of modern data processing tools*

- Memory;
- Processing power;

**Idea**
- Split tasks into subtasks;
- Distribute subtasks over several computers;
- Work together to finish task.

### Benefits of parallel computing

- Processing power;
- Memory: partition the dataset;

### Risks of parallel computing

*Overhead due to communication*

- Tasks needs to be large;
- Need several processing units;

## Parallel computation frameworks

### Hadoop

> "Hadoop is a collection of open source projects, maintained by the Apache Software Foundation. Some of them are bit outdated, but it's still relevant to talk about them."

Two Hadoop projects relevants:
- MapReduce
- HDFS

#### HDFS

> "HDFS is a distributed file system. Its similar to the file system of a computer, but the only difference being the files reside on multiple different computers. HDFS has been essential in the big data world, and for parallel computing by extension. Nowadays, cloud-managed storage systems like Amazon S3 often relplace HDFS."

#### MapReduce

> "MapReduce was one of the first popularized big-data processing paradigms. It works splitting tasks in subtasks, distributing the workload and data between several processing units. For MapReduce, these processing unitis are several computers in the cluster. MapReduce had its flaws; one of it was that it was hard to write these MapReduce jobs. Many software programas popped up to address this problem, and one of them was Hive."

##### Hive

> "Hive is a layer on top of the hadoop ecosystem that makes data from several sources queryable in a structured way using Hive's SQL variant: Hive SQL. Facebook initially developed Hive, but the Apache Software Foundation now maintains the project. Although MapReduce was initially responsible for runnig the Hive jobs, it now integrates with several other data processing tools."

##### Spark

> "The other parallel computation framework we'll introduce is called Spark. Spark distributes data processing tasks between clusters of computers. While MapReduce-based systems tend to need expensive disk writes between jobs, Spark tries to keep as much processing as possible in memory. In that sense, Spark was also an answer to the limitations of MapReduce. [...] Currently, the Apache Software Foundation maintains the project."

##### Resillient distributed datasets (RDD)

> "Spark's architecture relies on something called resilient distributed datasets, or RDDs. Without diving into technicalities, this is a data structure that maintains data which is distributed between multiple nodes. Unlike DataFrames, RDDs, don't have named columns. From a conceptual perspective, you can think of RDDs as lists of tuples. We can do two types of operations on these data structures: transformations, like map or filter, and actions, like count or first. Transformations result in transformed RDDs, while actions result in a single result."

##### PySpark

> "When working with Spark, people typically use a programming language interface like PySpark. PySpark is the Python interface to Spark. There are interfacese to Spark in other languages, like R or Scala, as well. PySpark hosts a DataFrame abstraction, which  means that you can do operations very similar to pandas DataFrames. PySpark and Spark take care of all the complex parallel computing operations."

## Workflow scheduling frameworks

### Pipeline

*How to schedule?*

- Manually;
- `cron` scheduling tool (what about dependencies between jobs?).

### DAGs

A great way to visualize dependencies between jobs is through Directed Acyclic Graphs, or DAGs. A DAG is a set of nodes that are connected by directed edges. There are no cycles in the graph, which means that no path following the directed edges sees a specific node more than once.~

### The tools for the job

- Linux tool, `cron`;
- Spotify's Luigi: allows for the definition of DAGs for complex pipelines;
- Apache Airflow.

### Apache Airflow

- Airbnb created Airflow as an internal tool for workflow management.
- They open-sourced Airflow in 2015, and it later joined Apache Software Foundation in 2016.
- They built Airflow around the concept of DAGs. Using Python, developers can create and test these DAGs that build up compex pipelines.
