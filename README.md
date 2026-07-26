# Retail Sales Data Cleaning Pipeline

## Overview

This project demonstrates an end-to-end **data cleaning pipeline** built using **Python, Pandas, and NumPy**. Three raw retail datasets (**Customers, Orders, and Products**) were merged into a single retail sales dataset, cleaned using business rules, standardized, and exported as an analysis-ready dataset.

---

# Dataset Summary

## Input Files

* Customers.xlsx
* Orders.xlsx
* Products.xlsx

## Dataset Size

### Before Cleaning

* **Rows:** 10,000
* **Columns:** 16

### After Cleaning

* **Rows:** 9,825
* **Columns:** 16

---

# Data Quality Summary

| Metric                |                Before |                      After |
| --------------------- | --------------------: | -------------------------: |
| Total Records         |                10,000 |                      9,825 |
| Missing Customer_ID   |                   497 |                          0 |
| Missing Product_ID    |                   175 |         0 *(rows removed)* |
| Missing Quantity      |                   316 |                          0 |
| Missing Gender        |                   790 |                          0 |
| Missing Age           |                   497 |                          0 |
| Missing City          |                   940 |                          0 |
| Missing State         |                   497 |                          0 |
| Missing Customer_Name |                   497 |                          0 |
| Missing Unit_Price    |                   790 |                          0 |
| Missing Product       |                   175 |                          0 |
| Missing Category      |                   175 |                          0 |
| Missing Brand         |                   175 |                          0 |
| Missing Join_Date     |                   497 |                        492 |
| Missing Order_Date    | 0 *(invalid strings)* | 2,556 *(converted to NaT)* |

> **Note:** Invalid `Order_Date` values were converted to `NaT` using `errors="coerce"`. These records were intentionally retained because they still contained meaningful customer and sales information for non-time-based analysis.

---

# Project Workflow

## 1. Data Integration

Merged three relational datasets using **Pandas `merge()`**.

* Orders + Customers
* Result + Products

---

## 2. Data Profiling

Performed initial data assessment using:

* `head()`
* `info()`
* `shape`
* `describe()`
* `isnull()`
* `duplicated()`

---

## 3. Missing Value Analysis

Calculated missing value counts and percentages to identify data quality issues before cleaning.

---

## 4. Date Conversion

Converted mixed-format date columns into datetime format.

Columns cleaned:

* Order_Date
* Join_Date

Used:

* `pd.to_datetime()`
* `errors="coerce"`
* `format="mixed"`

---

## 5. Text Standardization

Standardized inconsistent categorical values by:

* Removing leading/trailing spaces
* Standardizing Payment_Mode
* Standardizing Gender values

---

## 6. Data Validation

Applied business validation rules.

### Age

* Valid range: **18–100**

### Quantity

* Quantity must be **greater than or equal to 0**

Invalid values were replaced with `NaN`.

---

## 7. Missing Value Treatment

### Numerical Columns

* Median imputation for Age
* Median imputation for Quantity

### Categorical Columns

Filled missing values with **"Unknown"**

* Customer_ID
* Customer_Name
* City
* State
* Gender

### Product-Level Imputation

Filled missing **Unit_Price** using the median price of each product.

Implemented using:

* `groupby()`
* `transform()`

---

## 8. Record Filtering

Rows with missing **Product_ID** were removed because product information (Product, Category, Brand, and Unit Price) could not be recovered after merging.

Rows with missing **Order_Date** were retained because they still contained valid transactional information useful for product, customer, and revenue analysis.

---

## 9. Export

Exported the cleaned dataset to Excel.

---

# Pandas Functions Used

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

# NumPy Functions Used

* `np.nan`

---

# Key Achievements

* Merged **3 relational datasets** into a unified retail sales dataset.
* Processed **10,000 raw records** across **16 business attributes**.
* Removed **175 unrecoverable records** with missing Product_ID.
* Standardized date formats and categorical values.
* Applied business validation rules for Age and Quantity.
* Resolved missing values using median, product-level, and categorical imputation techniques.
* Exported a clean dataset containing **9,825 records** for downstream analytics.

---

# Repository Structure

```text
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

# Tech Stack

* Python
* Pandas
* NumPy
* Microsoft Excel

---

# Future Enhancements

* Exploratory Data Analysis (EDA)
* SQL-based Business Analysis
* Power BI Dashboard
* Customer Segmentation
* Sales Trend Analysis

---

# Author

**Rahul R Tiwari**

Aspiring Data Analyst | Python | SQL | Power BI | Excel
