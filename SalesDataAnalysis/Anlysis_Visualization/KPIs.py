import pandas as pd
import numpy as np
from cleaning.cleaning import fix_types

df = pd.read_csv('data/CleanedSuperStore.csv')


total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
avg_order_value = total_sales/total_orders


print(f"Total Sales: {total_sales}, Total Profit: {total_profit}, Total Orders: {total_orders}, AVG Order Value: {round(avg_order_value,2)}")