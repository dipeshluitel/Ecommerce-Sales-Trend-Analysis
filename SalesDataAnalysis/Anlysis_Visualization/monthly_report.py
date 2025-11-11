import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from KPIs import df


# creating time-series
ts = df.copy()

# makes Order Date as index
ts.set_index('Order Date', inplace=True)

#  Monthly Aggregation Starts here
monthly = ts[['Sales', 'Profit']].resample('M').sum()


# plotting

plt.figure(figsize=(12,5))
plt.plot(monthly.index, monthly['Sales'], label='Sales')
plt.plot(monthly.index, monthly['Profit'], label='Profit')
plt.title('Monthly Sales and Profit')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.legend()
plt.tight_layout()
plt.show()