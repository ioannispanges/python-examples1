import matplotlib.pyplot as plt
import pandas as pd

data = {'Month': ['Jan', 'Feb', 'Mar', 'Apl', 'May'],
        'Revenue': [500000, 600000, 500000, 600000, 620000]}
df = pd.DataFrame(data)

plt.plot(df['Month'], df['Revenue'], marker='o', linestyle='-', color='green')
plt.xlabel('Month')
plt.ylabel("Revenue (in Euros)")
plt.title('Trend in Monthly Revenue')
plt.show()
