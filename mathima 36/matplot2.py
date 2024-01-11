import matplotlib.pyplot as plt

time_point = [1, 2, 3, 4, 5]
values = [10, 25, 18, 35, 20]

plt.plot(time_point, values, marker='o', linestyle='-', color='green')
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Line Plot Example')
plt.show()
