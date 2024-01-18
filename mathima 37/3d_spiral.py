import matplotlib.pyplot as plt
import numpy as np

# dedomena
theta = np.linspace(0, 2 * np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
z = np.linspace(0, 1, 100)

# dimiourgia 3d plot

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# plotting
ax.plot(x, y, z, label='3D Spiral')
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
ax.set_title('3D Plot Example')
ax.legend()
plt.show()
