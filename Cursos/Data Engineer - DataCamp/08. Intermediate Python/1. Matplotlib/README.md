# Matplotlib

## Basic plots with Matplotlib

### Basic plots with Matplotlib

- Visualization
- Data Structure
- Control Structures
- Case study

### Data visualization

- Very important in Data Analysis
  - Explore data
  - Report insights
  
### Matplotlib

```python
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.show()
```

### Scatter plot

```python
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.scatter(year, pop)
plt.show()
```

## Histogram

### Histogram

- Explore dataset
- Get idea about distribution

### Matplotlib

```python
import matplotlib.pyplot as plt

print(help(plt.hist))

values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins=3)
plt.show()
```
## Customization

### Data visualization

- Many options
  - Different plot types
  - Many customizations
- Choice depends on
  - Data
  - Story you want to tell

### Population.py plot

```python
import matplotlib.pyplot as plt
year = [1950, 1951, 1952, ..., 2100]
pop = [2.538, 2.57, 2.62, ..., 10.85]

plt.plot(year, pop)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0, 2, 4, 6, 8, 10], ['0', '2B', '4B', '6B', '8B', '10B'])

plt.show()
```