# Importing Data From Excel Files

## Introduction to spreadsheets

### Spreadsheets

- Also known as Excel files;
- Data stored in tabular form, with cells arranged in rows and columns;
- Unlike flat files, can have formatting and formulas;
- Multiple spreadsheets can exist in a workbook;

### Loading Spreadsheets

- Spreadsheets have their own loading function in `pandas` : `read_excel()`

```python
import pandas as pd

# Read the Excel file
survey_data = pd.read_excel("fcc_survey.xlsx")

# View the first 5 lines of data
print(survey_data.head())
```

#### Loading Select Columns and Rows

- `read_excel()` has many keyword arguments in common with `read_csv()`
  - `nrows`: limit number of rows to load;
  - `skiprows`: specify number of rows or row numbers to skip;
  - `usecols`: choose columns by name, positional number, or letter (e.g. "A:P").

```python
# Read columns W-AB and AR of file, skipping metadata header
survey_data = pd.read_excel("fcc_survey_with_headers.xlsx",
							skiprows=2,
							usecols="W:AB, AR")
```

## Getting data from multiple worksheets

### Selecting Sheets to Load

- `read_excel()` loads the first sheet in an Excel file by default;
- Use the `sheet_name` keyword argument to load other sheets;
- Specify spreadsheets by name and/or (zero-indexed) position number;
- Pass a list of names/numbers to load more than one sheet at a time;
- Any arguments passed to `read_excel()` apply to all sheets read.

```python
# Get the second sheet by position index
survey_data_sheet2 = pd.read_excel('fcc_survey.xlsx',
								   sheet_name=1)

# Get the second sheet by name
survey_data_2017 = pd.read_excel('fcc_survey.xlsx',
								 sheet_name='2017')
```

### Loading all sheets

- Passing `sheet_name=None` to `read_excel()` reads all sheets in a workbook;

```python
survey_responses = pd.read_excel("fcc_survey.xlsx", sheet_name=None)
```

## Modifying imports: true/false data

### Boolean Data

- True / False data

### pandas and Booleans

- pandas loads True / False columns as float data by default
- Specify a column should be bool with `read_excel()`'s `dtype` argument
- Boolean columns can only have True and False values
- **NA/missing values in Boolean columns are changed to True**
- pandas automatically recognizes some values as True / False in Boolean columns
- Unrecognized values in a Boolean column are also changed to True

### Setting Custom True/False Values

- Use `read_excel()`'s `true_values` argument to set custom `True` values
- Use `false_values` to set custom `False` values
- Each takes a list of values to treat as `True`/`False`, respectively
- Custom True / False values are only applied to columns set as Boolean

### Boolean Considerations

- Are there missing values, or could there be in the future?
- How will this columns be used in analysis?
- What would happen if a value were incorrectly coded as True?
- Could the data be modeled another way (e.g., as float or integers)?

## Modifying imports: parsing dates

### Date and Time Data

- Dates and times have their own data type and internal representation
- Datetime values can be translated into string representations
- Common set of codes to describe datetime string formatting

### pandas and Datetimes

- Datetime columns are loaded as objects (strings) by default;
- Specify that columns have datetimes with the `parse_dates` argument (not `dtype`!)
- `parse_dates` can accept:
  - a list of column names or numbers to be parse
  - a list containing lists of columns to combine and parse
  - a dictionary where keys are new column names and vaalues are lists of columns to parse together

### Non-Standard Dates

- `parse-dates` doesn'ttt work with non-standard datetime formats
- Use `pd.to_datetime()` after loading data if `parse_dates` won't work
- `to_datetime()` arguments:
  - Data frame and column to convert
  - `format`: string representation of datetime format

### Datetime Formatting

- Describe datetime string formatting with codes and characters
- Refer to strftime.org for the full list

Code, meaning, example
- %Y, Year (4-digit), 1999
- %m, Month (zero-padded), 03
- %d, Day (zero-padded), 01
- %H, Hour (24-hour clock), 21
- %M, Minute (zero-padded), 09
- %S, Second (zero-padded), 05
