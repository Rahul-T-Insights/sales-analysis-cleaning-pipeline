# Load lib

import pandas as pd
import numpy as np

# Read file

Customers = pd.read_excel(r"C:\Users\hp\Desktop\Projects\Retail Sales Analysis\Customers.xlsx")
Orders = pd.read_excel(r"C:\Users\hp\Desktop\Projects\Retail Sales Analysis\Orders.xlsx")
Product = pd.read_excel(r"C:\Users\hp\Desktop\Projects\Retail Sales Analysis\Products.xlsx")

# Merge the dataset

sales = pd.merge(
    Orders,
    Customers,
    on = "Customer_ID",
    how = "left"
)

sales = pd.merge(
    sales,
    Product,
    on = "Product_ID",
    how = "left"
)

# Understand the data

print(sales.head())
sales.info()
print(sales.shape)
print(sales.describe())
print(sales.isnull().sum())

# Find duplicates, count and delete duplicate

print(sales.duplicated().sum())
print(sales["Product_ID"].isnull().sum())
sales = sales.dropna(subset=["Product_ID"])

# Analyze missing data

print("\nMissing values")
missing_percentage = (sales.isnull().sum() / len(sales))*100
print(missing_percentage.sort_values(ascending = False))

# convert datetime

sales["Order_Date"] = pd.to_datetime(
    sales["Order_Date"],
    format = "mixed",
    errors = "coerce",
    dayfirst = True
)

sales["Join_Date"] = pd.to_datetime(
    sales["Join_Date"],
    format = "mixed",
    errors = "coerce",
    dayfirst = True
)

# Standardize text

sales["Payment_Mode"] = sales["Payment_Mode"].str.strip().replace({
    "upi" : "UPI",
    "card" : "Card",
    "cash" : "Cash"
})

sales["Gender"] = sales["Gender"].str.strip().replace({
    "male": "Male",
    "female": "Female",
    "M": "Male",
    "F": "Female"
}).str.title()

# Data Validation

sales.loc[
    (sales["Age"] < 18 ) | (sales["Age"] > 100), "Age"
] = np.nan

sales.loc[
    (sales["Quantity"] < 0 ), "Quantity"
] = np.nan

# Handling missing values

sales["Customer_Name"] = sales["Customer_Name"].fillna("Unknown")
sales["Customer_ID"] = sales["Customer_ID"].fillna("Unknown")
sales["City"] = sales["City"].fillna("Unknown")
sales["Gender"] = sales["Gender"].fillna("Unknown")
sales["State"] = sales["State"].fillna("Unknown")

median_age = sales["Age"].median()
sales["Age"] =sales["Age"].fillna(median_age)

sales["Unit_Price"] = sales.groupby("Product")["Unit_Price"].transform(
    lambda x : x.fillna(x.median())
)

median_qty = sales["Quantity"].median()
sales["Quantity"] = sales["Quantity"].fillna(median_qty)

# verify

print(sales.head())
print(sales.isnull().sum())
print(sales.shape)

# import file

sales.to_excel(r"C:\Users\hp\Desktop\Projects\Retail Sales Analysis\Cleaned.xlsx",
index = False)

print("\n File Created")
