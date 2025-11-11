import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from KPIs import df

regional_sales = df.groupby('Region')[['Sales','Profit']].sum().sort_values('Sales',ascending=False)

print(regional_sales)

# Plot

plt.figure(figsize=(10,5))
sns.barplot(data=regional_sales,x='Sales',y='Region',orient='h')
plt.title("Regional Sales Comparision")
plt.tight_layout()
plt.show()

# regional_sales.to_csv('results/RegionalReport.csv')