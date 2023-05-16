# Importing data from other file types

## Introduction to other file types

### Other file types

- Excel spreadsheets
- MATLAB files
- SAS files
- Stata files
- HDF5 files

### Pickled files

- File type native to Python
- Motivation: many datatypes for which it isn't obvious how to store them
- Pickled files are serialized
- Serialize = convert object to bytestream

```python
import pickle
with open('pickled_fruit.pkl', mode='rb') as file:
    data = pickle.load(file)
print(data)
```

### Importing Excel spreadsheets

```python
import pandas as pd
file = 'urbanpop.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names)
df1 = data.parse('1960-1966')  # sheet name, as a string
df2 = data.parse(0) # sheet index, as a float
```

## Importing SAS/Stata files using pandas

### SAS and Stata files

- SAS: Statistical Analysis System
- Stata: "Statistics" + "data"
- SAS: business analytics and biostatistics
- Stata: academic social sciences research

### SAS files

- Used for:
    - Advanced analytics
    - Multivariate analysis
    - Business intelligence
    - Data management
    - Predictive analytics
    - Standard for computational analysis

### Importing SAS files

```python
import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT('urbanpop.sas7bdat') as file:
    df_sas = file.to_data_frame()
```

### Importing Stata files

```python
import data as pd
data = pd.read_stata('urbanpop.dta')
```

## Importing HDF5 files

### HDF5 files

- Hierarchical Data Format version 5
- Standard for storing large quantities of numerical data
- Datasets can be hundreds of gigabytes or terabytes
- HDF5 can scale to exabytes

```python
import h5py
filename = 'H-H1_LOSC_4_V1-815411200-4096.hdf5'
data = h5py.File(filename,'r') # 'r' is to read
print(type(data))
```

## Importing MATLAB files

### MATLAB

- "Matrix Laboratory"
- Indusrty standard in engineering and science
- Data saved as .mat files

### SciPy to the rescue!

- scipy.io.loadmat() - read .mat files
- scipy.io.savemat() - write .mat files

### Importing a .mat files

```python
import scipy.io
filename = 'workspace.mat'
mat = scipy.io.loadmat(filename)
print(type(mat)) # <class 'dict'>
```

- keys = MATLAB variable names
- values = objects assigned to variables