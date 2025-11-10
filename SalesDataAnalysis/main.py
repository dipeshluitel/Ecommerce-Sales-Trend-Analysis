import pandas as pd 
import numpy as np

df = pd.read_csv("sampleData/Superstore.csv", encoding="latin1")

# Converted the data types

# df['Order ID'] = df["Order ID"].astype("string")
# df['Order Date'] = pd.to_datetime(df["Order Date"], errors='coerce')
# df['Ship Date'] = pd.to_datetime(df["Ship Date"], errors='coerce')
# df['Customer ID'] = df['Customer ID'].astype("string")
# df['Customer Name'] = df["Customer Name"].astype("string")
# df['Country'] = df["Country"].astype("string")
# df['City'] = df["City"].astype("string")
# df['State'] = df["State"].astype("string")
# df['Postal Code'] = df["Postal Code"].astype("string")
# df['Region'] = df["Region"].astype("string")
# df['Product ID'] = df["Product ID"].astype("string")
# df['Category'] = df["Category"].astype("string")
# df['Sub-Category'] = df["Sub-Category"].astype("string")
# df['Product Name'] = df["Product Name"].astype("string")


# Creating new column

# df['Month']=df['Order Date'].dt.month
# df['Year']=df['Order Date'].dt.year


print(df.head())
