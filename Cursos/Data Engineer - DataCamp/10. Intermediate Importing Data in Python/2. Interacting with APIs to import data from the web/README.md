# Interacting with APIs to import data from the web

## Introduction to APIs and JSONs

### APIs

- Application Programming Interface
- Protocols and routines
  - Building and interacting with software applications
  
### JSONs 

- JavaScript Object Notation
- Real-time server-to-browser communication

### Loading JSONs in Python

```python
import json
with open('snakes.json', 'r') as json_file:
    json_data = json.load(json_file)
    
print(type(json_data))

# Exploring JSONs in Python
for key, value in json_data.items():
    print(key + ':', value)
```

## APIs and interacting with the world wide web

### What is an API?

- Set of protocols and routines
- Bunch of code
  - Allows two software programs to communicate with each other
  
### Connecting to an API in Python

```python
import requests
url = 'http://www.omdbapi.com/?t=hackers'
r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
    print(key + ':', value)
```

### What was that URL?

- http - making an HTTP request
- www.omdbapi.com  - querying the OMDB API
- `?t=hackers`
  - Query string
  - Return data for a movie with title (t) 'Hackers'

`http://www.omdbapi.com/?t=hackers`