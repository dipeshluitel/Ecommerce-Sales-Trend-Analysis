import pandas as pd
import numpy as np

df = pd.read_csv('data/CleanedSuperStore.csv')

def fix_types(df):
    df['Order ID'] = df["Order ID"].astype("string")
    df['Order Date'] = pd.to_datetime(df["Order Date"], errors='coerce')
    df['Ship Date'] = pd.to_datetime(df["Ship Date"], errors='coerce')
    df['Customer ID'] = df['Customer ID'].astype("string")
    df['Customer Name'] = df["Customer Name"].astype("string")
    df['Country'] = df["Country"].astype("string")
    df['City'] = df["City"].astype("string")
    df['State'] = df["State"].astype("string")
    df['Postal Code'] = df["Postal Code"].astype("string")
    df['Region'] = df["Region"].astype("string")
    df['Product ID'] = df["Product ID"].astype("string")
    df['Category'] = df["Category"].astype("string")
    df['Sub-Category'] = df["Sub-Category"].astype("string")
    df['Product Name'] = df["Product Name"].astype("string")

fix_types(df)

if __name__ == '__main__':
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    total_orders = df['Order ID'].nunique()
    avg_order_value = total_sales/total_orders

if __name__ == '__main__':
    print(f"Total Sales: {total_sales}, Total Profit: {total_profit}, Total Orders: {total_orders}, AVG Order Value: {round(avg_order_value,2)}")