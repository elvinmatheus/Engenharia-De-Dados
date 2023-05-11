# Case study - Hacker Statistics

## Random numbers

### Random generators

```python
import numpy as np

# np.random.rand() # pseudo-random numbers

np.random.seed(123) # starting from a seed

np.random.rand()

np.random.rand()
```

### Coin toss

```python
import numpy as np

np.random.seed(123)
coin = np.random.randint(0, 2) # Randomly generate 0 or 1
print(coin)
if coin == 0:
    print("heads")
else:
    print("tails")
```

## Random walk

### Heads or Tails

```python
import numpy as np
np.random.seed(123)
outcomes = []

for x in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")
print(outcomes)
```

### Heads or Tails: random walk

```python
import numpy as np
np.random.seed(123)
tails = [0]
for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)
print(tails)    
```

## Distribution

### Random Walk

```python
import numpy as np
np.random.seed(123)
tails = [0]
for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)
```

### 100 runs

```python
import numpy as np
np.random.seed(123)
final_tails = []
for x in range(100) :
    tails = [0]
    for x in range(10) :
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
print(final_tails)
```

### Histogram, 100 runs

```python
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
final_tails = []
for x in range(100) : # com 1000 ou 10000 a amostra fica melhor
    tails = [0]
    for x in range(10) :
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
plt.hist(final_tails, bins = 10)
plt.show()
```
