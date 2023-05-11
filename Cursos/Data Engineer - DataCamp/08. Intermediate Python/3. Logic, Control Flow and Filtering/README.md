# Logic, Control Flow and Filtering

## Comparison Operators

### NumPy recap

```python
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
bmi

print(bmi > 23)

print(bmi[bmi > 23])
```

- Comparison operators: how Python values relate

### Numeric comparisons

```python
print(2 < 3)
print(2 == 3)
print(2 <= 3)
print(3 <= 3)

x = 2
y = 3

print(x < y)
```

### Other comparisons

```python
print("carl" < "chris")
print(3 < "chris")
print(3 < 4.1)
```


### Comparators

| Comparator | Meaning               |
| ---------- | --------------------- |
| `<`        | Strictly less than    |
| `<=`       | Less than or equal    |
| `>`        | Strictly greater than |
| `>=`       | Greater than or equal |
| `==`       | Equal                 |
| `!=`       | Not equal             |

## Boolean operators

### Boolean operators

- `and`
- `or`
- `not`

### and

```python
print(True and True)

print(False and True)

print(True and False)

print(False and False)

x = 12
print(x > 5 and x < 15)
```

### or 

```python
print(True or True)

print(False or True)

print(True or False)

print(False or False)

y = 5
print(y < 7 or y > 13)
```

### not

```python
print(not True)

print(not False)
```

### NumPy

```python
print(bmi > 21 and bmi > 22) # ValueError
```

- `logical_and()`
- `logical_or()`
- `logical_not()`

```python
print(np.logical_and(bmi > 21, bmi < 22))

print(bmi[np.logical_and(bmi > 21, bmi < 22)])
```

## if, elif, else

### Overview

- Comparison Operators
  - `<`, `>`, `>=`, `<=`, `==`, `!=`
- Boolean Operators
  - `and`, `or`, `not`
- Conditional Statements
  - `if`, `else`, `elif`

### if

```python
if condition:
    expression
```
- `expression` not part of if

### else

```python
if condition:
    expression
else:
    expression
```

### elif

```python
if condition:
    expression
elif condition:
    expression
else:
    expression
```

## Filtering pandas DataFrames

### brics: select countries with area over 8 million km2

- 3 steps
  - Select the area column
  - Do comparison on area column
  - Use result to select countries
  
```python
import pandas as pd

brics = pd.read_csv("path/to/brics.csv", index_col = 0)

print(brics)

# brics["area"]
# area = brics.loc[:, "area"]
# brics.iloc[:, 2]

is_huge = brics["area"] > 8

brics[is_huge]
# brics[brics["area"] > 8]
```

### Boolean operators

```python
import numpy as np

np.logical_and(brics["area"] > 8, brics["area"] < 10)

brics[np.logical_and(brics["area"] > 8, brics["area"] < 10)]
```