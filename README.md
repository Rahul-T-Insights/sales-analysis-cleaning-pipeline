# Retail Sales Data Cleaning Pipeline using Python

## Project Overview

This project demonstrates an end-to-end **data cleaning pipeline** built using **Python, Pandas, and NumPy**. Three raw retail datasets (Customers, Orders, and Products) were merged into a single analytical dataset and cleaned using business rules, missing value treatment, and data standardization techniques.

The final output is an **analysis-ready dataset** that can be used for reporting, visualization, or further business analysis.

---

## Dataset

The project consists of three Excel files:

- Customers.xlsx
- Orders.xlsx
- Products.xlsx

After merging, the final dataset contains:

- **10,000 rows**
- **16 columns**
- Customer, Product, and Order information

---

## Technologies Used

- Python
- Pandas
- NumPy
- Excel

---

## Project Workflow

### 1. Data Import

- Loaded three Excel datasets using Pandas.

### 2. Data Integration

- Merged Customers, Orders, and Products datasets using:
  - `pd.merge()`
  - Left Join

### 3. Data Profiling

Performed initial data exploration using:

- `head()`
- `info()`
- `shape`
- `describe()`
- `isnull()`
- `duplicated()`

### 4. Date Cleaning

Converted mixed-format date columns into datetime format.

- Order_Date
- Join_Date

Used:

```python
pd.to_datetime()
```

### 5. Text Standardization

Standardized categorical columns by:

- Removing extra spaces
- Fixing inconsistent text values
- Standardizing Payment Mode
- Standardizing Gender

Used:

- `str.strip()`
- `replace()`

### 6. Data Validation

Applied business validation rules.

- Age between **18–100**
- Quantity greater than or equal to **1**

Invalid values were replaced with missing values.

### 7. Missing Value Treatment

Handled missing values using different strategies.

Numerical Columns

- Median Imputation

Categorical Columns

- Filled missing Customer_ID
- Filled missing City

Product Price

- Product-wise Median Imputation using:

```python
groupby().transform()
```

### 8. Export

Exported the cleaned dataset to Excel.

---

## Pandas Functions Used

- read_excel()
- merge()
- head()
- info()
- describe()
- shape
- isnull()
- duplicated()
- to_datetime()
- replace()
- str.strip()
- loc[]
- fillna()
- groupby()
- transform()
- median()
- to_excel()

---

## Project Highlights

- Merged **3 relational datasets**
- Cleaned a **10,000-row retail dataset**
- Standardized categorical and date fields
- Applied business validation rules
- Performed missing value imputation
- Exported an analysis-ready dataset

---

## Project Structure

```
Retail Sales Analysis/
│
├── Customers.xlsx
├── Orders.xlsx
├── Products.xlsx
├── Cleaned.xlsx
├── Retail sales analysis cleaning pipeline.py
└── README.md
```

---

## Future Improvements

- Exploratory Data Analysis (EDA)
- Sales Trend Analysis
- Customer Segmentation
- Power BI Dashboard
- SQL Data Analysis
- Interactive Visualizations

---

## Author

**Rahul R Tiwari**

Aspiring Data Analyst | Python | SQL | Power BI | Excel





