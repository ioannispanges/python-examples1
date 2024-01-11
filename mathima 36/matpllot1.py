import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C']
values = [25, 40, 30]

plt.bar(categories, values, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()
