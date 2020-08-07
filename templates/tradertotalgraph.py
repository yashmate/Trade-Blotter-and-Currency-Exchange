import matplotlib.pyplot as plt
import pandas as pd
df1=pd.read_csv('totalamount.csv')
plt.bar(df1['TRADER'],df1['TOTAL'], label="",color='g')
plt.xlabel('TRADER')
plt.ylabel('TOTAL AMOUNT TRADED')
plt.title('TRADE ANALYSIS')
plt.savefig('trader.jpg')

