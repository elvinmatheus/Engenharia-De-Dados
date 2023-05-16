# Working with relational databases in Python

## Introduction to relational databases

### Relational model

- Widely adopted 
- Codd’s 12 Rules/Commandments
    - Consists of 13 rules (zero-indexed!)
    - Describes what a Relational Database Management
    - System should adhere to to be considered relational

## Creating a database engine in Python

### Creating a database engine

- SQLite database
  - Fast and simple
- SQLAlchemy 
  - Works with many Relational Database Management Systems
  
```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Northwind.sqlite')
table_names = engine.table_names()
print(table_names)
```

## Querying relational databases in Python

- We'll use SQLAlchemy and pandas

### Workflow of SQL querying 

- Importing packages and functions
- Create the database engine
- Connect to the engine
- Query the database
- Save the query results to a DataFrame
- Close the connection

```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Northwind.sqlite')
con = engine.connect()
rs = con.execute("SELECT * FROM Orders")
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys() # define as colunas do dataframe
con.close()

print(df.head())
```

### Using the context manager

```python
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')

with engine.connect() as con:
    rs = con.execute("SELECT OrderID, OrderDate, ShipName FROM Orders")
    df = pd.DataFrame(rs.fetchmany(size=5))
    df.columns = rs.keys()
```

## Querying relational databases directly with pandas

### The pandas way to query

```python
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Orders")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    
df = pd.read_sql_query("SELECT * FROM Orders", engine) # Alternativa
```

## Advanced querying: exploiting table relationships

### INNER JOIN in Python (pandas)

```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Northwind.sqlite')
df = pd.read_sql_query("SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID", engine)
print(df.head())
```