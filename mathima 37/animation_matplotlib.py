import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y, color='blue')


def update(frame):
    line.set_ydata(np.sin(x + frame * 0.1))
    return line,


animation = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Animate Sinusoidal Wave')
plt.show()
