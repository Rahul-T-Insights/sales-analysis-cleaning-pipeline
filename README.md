# Retail Sales Data Cleaning Pipeline

## Overview

This project demonstrates an end-to-end **data cleaning pipeline** using **Python, Pandas, and NumPy**. Three raw retail datasets (**Customers, Orders, and Products**) were merged into a unified dataset, cleaned using business rules, standardized for consistency, and prepared for downstream analytics.

The final cleaned dataset contains **9,825 records** and is ready for exploratory data analysis, SQL queries, dashboard development, and business reporting.

---

## Dataset

The project uses three Excel datasets:

* **Customers.xlsx**
* **Orders.xlsx**
* **Products.xlsx**

These were merged using **left joins** on `Customer_ID` and `Product_ID`.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Microsoft Excel

---

## Data Cleaning Workflow

### 1. Data Integration

* Loaded three Excel datasets using Pandas.
* Merged datasets with `pd.merge()` to create a unified sales table.

### 2. Data Profiling

Performed an initial assessment using:

* `head()`
* `info()`
* `shape`
* `describe()`
* `isnull()`
* `duplicated()`

### 3. Missing Value Analysis

Calculated missing value percentages for every column to identify data quality issues before cleaning.

### 4. Date Standardization

Converted mixed-format date columns into datetime format using:

* `Order_Date`
* `Join_Date`

Invalid or unreadable dates were converted to `NaT` using `errors="coerce"`.

### 5. Text Standardization

Cleaned inconsistent categorical values by:

* Removing leading/trailing spaces
* Standardizing payment modes
* Standardizing gender values

### 6. Business Rule Validation

Applied validation rules to improve data quality:

* Valid Age: **18–100**
* Quantity must be **greater than or equal to 0**

Invalid values were replaced with `NaN` before imputation.

### 7. Missing Value Treatment

Applied different strategies based on data type.

**Numerical Columns**

* Median imputation for Age
* Median imputation for Quantity

**Categorical Columns**

* Filled missing Customer_ID with `"Unknown"`
* Filled missing Customer_Name with `"Unknown"`
* Filled missing City with `"Unknown"`
* Filled missing State with `"Unknown"`
* Filled missing Gender with `"Unknown"`

**Product Price**

* Filled missing `Unit_Price` using **product-level median imputation** with `groupby()` and `transform()`.

### 8. Record Filtering

Rows with missing `Product_ID` were removed because product information (Product, Category, Brand, and Unit Price) could not be recovered after merging.

Rows with missing `Order_Date` were intentionally retained because they still contained meaningful customer, product, and transaction information useful for non-time-based analysis.

### 9. Export

Exported the cleaned dataset to Excel for further analysis.

---

## Pandas Functions Used

* `read_excel()`
* `merge()`
* `head()`
* `info()`
* `describe()`
* `shape`
* `isnull()`
* `duplicated()`
* `to_datetime()`
* `replace()`
* `str.strip()`
* `loc[]`
* `fillna()`
* `groupby()`
* `transform()`
* `median()`
* `dropna()`
* `to_excel()`

---

## Project Summary

* Merged **3 relational datasets** into a unified retail sales dataset.
* Processed **10,000 raw records**.
* Delivered a cleaned dataset containing **9,825 records**.
* Standardized date and categorical fields.
* Validated business rules for numerical data.
* Applied median, product-level, and categorical imputation techniques.
* Preserved valuable transaction records while removing unrecoverable product records.
* Exported an analysis-ready dataset for reporting and visualization.

---

## Repository Structure

```
Retail Sales Analysis/
│
├── Customers.xlsx
├── Orders.xlsx
├── Products.xlsx
├── Cleaned.xlsx
├── sales_analysis_cleaning_pipeline.py
└── README.md
```

---

## Future Improvements

* Exploratory Data Analysis (EDA)
* SQL-based business analysis
* Power BI dashboard
* Customer segmentation
* Sales trend analysis
* Product performance analysis

---

## Author

**Rahul R Tiwari**

Aspiring Data Analyst | Python | SQL | Power BI | Excel
