import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'value':[1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
df = pd.DataFrame(data)
#df['value'].hist()
df.boxplot(by = 'value', column='value')
plt.show()



plt.show()
df = pd.DataFrame(data)

dates = pd.date_range(start='2022-07-26', periods=10, freq='D')
values = np.random.rand(10)
df = pd.DataFrame({'Date': dates, 'Value': values})
df.set_index('Date', inplace=True)
month = df.resample('M').mean()
print(df)
print()
print(month)
