# Introduction and flat files

## Flat files

### Import data

- Flat files, e.g., .txt, .csv
- Files form other software
- Relational databases

### Reading a text file

```python
filename = "huck_finn.txt"
file = open(filename, mode='r') # 'r' is to read
text = file.read()
file.close()
print(text)
```

### Writing to a file

```python
filename = 'huck_finn.txt'
file = open(filename, mode='w') # 'w' is to write
file.close()
```

### Context manager with

```python
with open('huck_finn.txt', mode='r') as file:
    print(file.read())
```

## The importance of flat files in data science

### Flat files

- Text files containing records
- That is, table data
- Record: row of fields or attributes
- Column: feature or attribute

### File extension

- .csv - Comma separated values
- .txt - Text file
- commas, tabs - Delimiters

### How do you import flat files?

- Two main packages: NumPy, pandas

## Importing flat files using NumPy

### Why NumPy?

- NumPy arrays: standard for storing numerical data
- Essential for other packages: e.g. scikit-learn
- loadtxt()
- genfromtxt()

### Importing flat files using NumPy

```python
import numpy as np
filename = 'MNIST.txt'
data = np.loadtxt(filename, delimiter=',')
print(data)
```

### Customizing your NumPy import

```python
import numpy as np
filename = 'MNIST_header.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=1)
print(data)
```

```python
import numpy as np
filename = 'MNIST_header.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0, 2])
print(data)
```

```python
data = np.loadtxt(filename, delimiter=',', dtype=str)
```

## Importing flat files using pandas

### What a data scientist needs

- Two-dimensional labeled data structure(s)
- Columns of potentially different types 
- Manipulate, slice, reshape, groupby, join, merge
- Perform statistics
- Work with time series data

### Manipulating pandas DataFrames

- Exploratory data analysis
- Data wrangling
- Data preprocessing
- Building models
- Visualization
- Standard and best practice to use pandas

### Importing using pandas

```python
import pandas as pd
filename = 'winequality-red.csv'
data = pd.read_csv(filename)
data.head()
```