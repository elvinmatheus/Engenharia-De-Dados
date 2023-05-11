# Dictionaries and Pandas

## Dictionaries, part 1

### Dictionary

```python
world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
print(world["albania"])
```

## Dictionaries, part 2

### Keys

- Keys have to be "immutable" objects

```python
dicio = {0:"hello", True:"dear", "two":"world"}
```

### List vs Dictionary

| List                                 | Dictionary                           |
|--------------------------------------|--------------------------------------| 
| Select, update, and remove with `[]` | Select, update, and remove with `[]` |
| Indexed by range of numbers          | Indexed by unique keys               |
| Collection of values - order matters, 
for selecting entire subsets           | Lookup table with unique keys        |

## Pandas, part 1

### Datasets in Python

- 2D NumPy array?
  - One data type
  
- pandas!
  - High level data manipulation tool
  - Wes McKinney
  - Built on NumPy
  - DataFrame
  
### DataFrame from Dictionary

```python
import pandas as pd

dict = {
"country":["Brazil","Russia","India","China","South Africa"],
"capital":["Brasilia","Moscow","New Delhi","Beijing","Pretoria"],
"area":[8.516, 17.10, 3.286, 9.597, 1.221],
"population":[200.4, 143.5, 1252, 1357, 52.98] }

brics = pd.DataFrame(dict)

print(brics)

brics.index = ["BR", "RU", "IN", "CH", "SA"]

print(brics)
```

- Keys (column labels)
- values (data, column by column)

### DataFrame from CSV file

`brics.csv`

```csv
,country,capital,area,population
BR,Brazil,Brasilia,8.516,200.4
RU,Russia,Moscow,17.10,143.5
IN,India,New Delhi,3.286,1252
CH,China,Beijing,9.597,1357
SA,South Africa,Pretoria,1.221,52.98
```

- CSV = comma-separated values

```python
brics = pd.read_csv("path/to/brics.csv", index_col = 0)
print(brics)
```

## Pandas, part 2

### Index and select data

- Square brackets
- Advanced methods
  - loc
  - iloc
  
### Column access []

```python
print(brics["country"])

print(type(brics["country"])) # pandas.core.series.Series

print(brics[["country"]])

print(type(brics[["country"]])) # pandas.core.frame.DataFrame

print(brics[["country", "capital"]])
```

### Row access []

```python
print(brics[1:4])
```

### Discussion []

- Square brackets: limited functionality
- Ideally
  - 2D NumPy arrays
  - my_array[rows, columns]
- pandas
  - `loc` (label-based)
  - `iloc` (integer position-based)
  
### Row Access loc

```python
print(brics.loc["RU"]) # row as pandas series

print(brics.loc[["RU"]]) # dataframe

print(brics.loc[["RU", "IN", "CH"]])

```

### Row and Column loc

```python
print(brics.loc[["RU", "IN", "CH"], ["country", "capital"]])

print(brics.loc[:, ["country", "capital"]])
```

### Recap

- Square brackets
  - Column access: `brics[["country", "capital"]]`
  - Row access: only through slicing `brics[1:4]`
- loc (label-based)
  - Row access `brics.loc[["RU", "IN", "CH"]]`
  - Column access `brics.loc[:, ["country", "capital"]]`
  - Row and column access `brics.loc[["RU", "IN", "CH"], ["country", "capital"]]`
  
### Row Access iloc

```python
print(brics.iloc[[1]])
print(brics.iloc[[1, 2, 3]])
```

### Row and Column iloc

```python
print(brics.iloc[[1, 2, 3], [0, 1]])
print(brics.iloc[:, [0, 1]])
```