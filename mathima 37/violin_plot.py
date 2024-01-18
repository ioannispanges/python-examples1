import seaborn as sns
import matplotlib.pyplot as plt

# eisagwgi dedomenwn apo bibliothiki seaborn

data = sns.load_dataset("tips")

# dimiourgia plot violin

sns.violinplot(x='day', y="total_bill", data=data, palette="muted")
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.title('Violin Plot Example')
plt.show()
