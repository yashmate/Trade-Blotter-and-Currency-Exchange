import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('exchangerates.csv')
print(df.columns)
plt.plot(df['Unnamed: 0'],df['EXCHANGE_RATE'],'g',label='RATE', linewidth=5)
plt.title('CURRENCY INFO')
plt.ylabel('RATE')
plt.xlabel('DAYS')
plt.legend()
plt.grid(True,color='k')
plt.savefig('exchangegraph.png')
plt.show()
