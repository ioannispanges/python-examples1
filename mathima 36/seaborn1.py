import seaborn as sns
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [10, 25, 18, 35, 20]

sns.scatterplot(x=x_values, y=y_values, color='red')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Scatter Plot Example')
plt.show()
