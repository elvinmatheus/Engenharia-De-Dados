# Importing data from the Internet

## Importing flat files from the web

### The urllib package

- Provides interface for fetching data across the web
- `urlopen()` - accepts URLs instead of file names

### How to automate file download in Python

```python
from urllib.request import urlretrieve
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
urlretrieve(url, 'winequality-white.csv')
```

## HTTP requests to import files from the web

### URL

- Uniform/Universal Resource Locator
- References to web resources
- Focus: web addresses
- Ingredients:
  - Protocol identifier - http:
  - Resource name - datacamp.com
- These specy web addresses uniquely

### HTTP

- HyperText Transfer Protocol
- Foundation of data communication for the web
- HTTPS - more secure form of HTTP
- Going to a website = sending HTTP request
  - GET request
- `urlretrieve()` performs a GET request
- HTML - HyperText Markup Language

### GET requests using urllib

```python
from urllib.request import urlopen, Request

url = "https://www.wikipedia.org/"
request = Request(url)
response = urlopen(request)
html = response.read()
response.close()
```

### GET requests using requests

- One of the most downloaded Python packages

```python
import requests
url = "https://www.wikipedia.org/"
r = requests.get(url)
text = r.text
```

## Scraping the web in Python

### HTML 

- Mix of unstructured and structured data
- Structured data:
  - Has pre-defined data mode, or
  - Organized in a defined manner
- Unstructured data: neither of these properties

### BeautifulSoup

- Parse and extract structured data from HTML
- Make tag soup beautiful and extract information

```python
from bs4 import BeautifulSoup
import requests
url = 'https://www.crummy.com/software/BeautifulSoup/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)

print(soup.prettify())
print(soup.title)
print(soup.get_text())

for link in soup.find_all('a'):
    print(link.get('href'))
```