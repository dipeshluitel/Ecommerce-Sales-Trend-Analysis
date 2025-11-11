import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from KPIs import df

#  TOP 10 best selling products

top_product = df.groupby('Product Name')[['Sales','Profit']].sum().sort_values('Sales', ascending=False).head(10)
top_product.reset_index

print(top_product)

#  Plot

plt.figure(figsize=(10,5))
sns.barplot(data=top_product, x='Sales', y='Product Name', orient='h')
plt.title("Top 10 Products of all time by Sales")
plt.tight_layout()
plt.show()

# top_product.to_csv('results/Top10products.csv')