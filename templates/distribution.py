import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('totalamount.csv')
slices = df['TOTAL']
activities = df['TRADER']
plt.pie(slices,
        labels=activities,
        startangle=90,
        autopct='%1.1f%%')
plt.title('DISTRIBUTION DURING THE DAY')
plt.savefig('distribution.jpg')
plt.show()
