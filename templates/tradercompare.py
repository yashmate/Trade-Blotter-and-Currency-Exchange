import matplotlib.pyplot as plt
import pandas as pd
df1=pd.read_csv('stevetrader.csv')
df2=pd.read_csv('warrentrader.csv')
width = 0.35       
plt.bar(df1['DAY'], df1['AMOUNT'], width, label='STEVE')
plt.bar(df1['DAY'] + width, df2['AMOUNT'], width,
    label='Warren')
plt.ylabel('Amount Traded')
plt.title('COMPARATIVE ANALYSIS')
plt.legend(loc='best')
plt.savefig('compare.jpg')
