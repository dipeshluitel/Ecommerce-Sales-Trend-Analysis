import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from KPIs import df

cat_sales = df.groupby('Category')[['Sales','Profit']].sum().sort_values('Sales', ascending=False)

# plot category sales
plt.figure(figsize=(10,5))
sns.barplot(data=cat_sales, x='Sales',y='Category', orient='h')
plt.title("Top Products By Categories")
plt.tight_layout()
plt.show()

# subcategory
sub_sales = df.groupby('Sub-Category')[['Sales','Profit']].sum().sort_values('Sales', ascending=False).head(15)
sub_sales['Sales'].plot(kind='bar', figsize=(10,5))
plt.title('Top Sub-Categories by Sales (Top 15)')
plt.tight_layout()
plt.show()

# cat_sales.to_csv("TopProductByCategory.csv")
# sub_sales.to_csv("TopProductBySubCategory.csv")
