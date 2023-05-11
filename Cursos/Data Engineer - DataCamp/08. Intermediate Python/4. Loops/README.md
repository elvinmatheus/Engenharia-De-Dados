# Loops

## while loop

### if-elif-else

- Goes through construct only once

- While loop = repeated if statement

### While

```python
while condition:
    expression
```

- Numerically calculating model
- "repeating action until condition is met"

## for loop

### for loop

```python
for var in seq:
    expression
```

- "for each var in seq, execute expression"

### enumerate

```python
fam = [1.73, 1.68, 1.71, 1.89]

for index, height in enumerate(fam):
    print("index " + str(index) + ": " + str(height))
```

### Loop over string

```python
for c in "family":
    print(c.capitalize())
```

## Loop data structures part 1

### Dictionary

```python
for key, value in world.items():
    print(key + "--" + str(value))
```

### NumPy

```python
import numpy as np
np_
height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
for val in bmi :
print(val)
```

### 2D NumPy Arrays

```python
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight])
for val in meas :
print(val)
```

```python
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight])
for val in np.nditer(meas) : # itera sobre cada elemento do array
print(val)
```

## Loop Data Structures part 2

### for, first try

```python
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
for val in brics: # imprime o nome das colunas
    print(val)
```

### iterrows

```python
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
for lab, row in brics.iterrows():
    print(lab) # imprime label da linha
    print(row) # imprime linha atual (ex.: Brasil)
```

### Selective print

```python
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"])
```

### Add column

```python
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
for lab, row in brics.iterrows() :
    # - Creating Series on every iteration
    brics.loc[lab,"name_length"] = len(row["country"])
print(brics)
```

### apply

```python
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
brics["name_length"] = brics["country"].apply(len)
print(brics)
```