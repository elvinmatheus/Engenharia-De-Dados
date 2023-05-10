#  Python lists

## Python data types

- float - real numbers
- int - integer numbers
- str - string, text
- bool - True, False
- Each variable represents single value

### Python list

- Name a collection of values
- Contain any type
- Contain different types

### List type

- Specific functionality
- Specific behavior

## Subsetting lists

### Subsetting lists

```python
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

fam

quarto = fam[3] # quarto elemento da lista

fam [-1] # último elemento da lista
```

### List slicing

```python
fam[3:5]

fam[1:4]

# [start (inclusive) : end (exclusive) ]

fam[:4]

fam[5:]
```

## Manipulating Lists

### List Manipulation

- Change list elements
- Add list elements
- Remove list elements

#### Changing list elements

```python
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam[7] = 1.86
fam[0:2] = ["lisa", 1.74]
print(fam)
```

#### Adding and removing elements

```python
fam + ["me", 1.79]
del(fam[2])
```

#### Behind the scenes

```python
x = ["a", "b", "c"]
y = list(x) #1: metodo copia lista
y = x[:] #2: metodo copia lista
y[1] = "z"
print(x)
print(y)
```