# NumPy

## NumPy

- Numeric Python
- Alternative to Python List: NumPy Array
- Calculations over entire arrays
- Easy and Fast
- Installation
  - In the terminal: pip3 install numpy
  
### Example

```python
import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
```

### NumPy: remarks

- NumPy arrays: contain only one type
- Different types: different behavior!

### NumPy Subsetting

```
um_elemento = bmi[1]
vetor_booleano = bmi > 23
subvetor = bmi[bmi > 23]
```

## 2D NumPy Arrays

### Type of NumPy Arrays

```python
import numpy as np

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
               [65.4, 59.2, 63.6, 88.4, 68.7]])

print(np_2d.shape)

subsetting1 = np_2d[0]

subsetting2 = np_2d[0][2]

subsetting3 = np_2d[0, 2]

interval1 = np_2d[:, 1:3]

interval2 = np_2d[1, :]
```

## NumPy: Basic Statistics

### Data analysis

- Get to know your data 
- Little data -> simply look at it
- Big data -> ?

### City-wide survey

```python
import numpy as np
np_city = ... # Implementation left out

np.mean(np_city[:, 0])

np.median(np_city[:, 0])

np.corrcoef(np_city[:, 0], np_city[:, 1])

np.std(np_city[:, 0])
```

- sum(), sort(), ...
- Enforce single data type: speed!

### Generate data

- Arguments for np.random.normal()
  - distribution mean
  - distribution standard deviation
  - number of samples
  
```python
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)

weight = np.round(np.random.normal(60.32, 15, 5000), 2)

np_city = np.column_stack((height, weight))
```