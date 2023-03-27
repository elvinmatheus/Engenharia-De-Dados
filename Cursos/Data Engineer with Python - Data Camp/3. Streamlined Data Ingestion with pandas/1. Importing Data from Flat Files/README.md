# Importing Data from Flat Files

## Introduction to Flat Files

### Pandas

- Python's library;
- Developed by Wes McKinney in 2008;
- Makes it easy to load and manipulate data, and it integrates with loads of analysis and visualization libraries.

#### Data Frames

Pandas specific structure for two-dimensional data;

> "This means that they have columns, typically labeled with variable names, and names, which also have labels, known as an index in pandas. The default index is the row number, but we can specify a column as the index, and many types of data can be used.

#### Flat Files

- Simple, easy-to-produce format;
- Data stored as plain text (no formatting);
- One row per line;
- Values for different fields are separated by a delimitter;
- Most common flat file type: comma-separated values;
- One `pandas` function to load them all: `read_csv()`.

Example:

```python
import pandas as pd

tax_data = pd.read_csv("us_tax_data_2016.csv")
tax_data.head(3)
```

In case of a different delimiter:

```python
import pandas as pd

tax_data = pd.read_csv("us_tax_data_2016.csv", sep="\t")
tax_data.head(3)
```

## Modifying flat file imports

### Limiting Columns

- Choose columns to load with the `usecols` keyword argument;
- Accepts a list of column numbers or names, or a function to filter column names.

### Limiting Rows

- Limit the number of rows loaded with the `nrows` keyword argument.
- Use `nrows` and `skiprows` to process a file in chunks;
- `skiprows` accepts a list of row numbers, a number of rows, or a function to filter rows;
- Set `header=None` so `pandas` knows there are no column names.

### Assigning Column Names

- Supply column names by passing a list to the `names` argument;
- The list **MUST** have a name for every column in your data;
- **If you only need to rename a few columns, do it after the import!**.

## Handling errors and missing data

### Common Flat File Import Issues

- Column data types are wrong;
- Values are missing;
- Records that cannot be read by pandas.

### Specifying Data Types

- `pandas` automatically infers column data types;
- Use the `dtype` keyword argument to specify column data types;
- `dtype` takes a dictionary of column names and data types.

### Customizing Missing Data Values

- `pandas` automatically interprets some values as missing or NA;
- Use the `na_values` keyword argument to set custom missing values;
- Can pass a single value, list, or dictionary of columns and values.

### Lines with Errors

- Set `error_bad_lines=False` to skip unparseable records;
- Set `warn_bad_lines=True` to see messages when records are skipped.
