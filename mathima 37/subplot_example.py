import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
# dimiourgia subplot
figs, axs = plt.subplots(2, 1, figsize=(8, 6))

# proto diagramma
axs[0].plot(x, y1, color='blue', label='sin(x)')
axs[0].set_title('Subplot 1')
# label tou sin(x)
axs[0].legend()

# deutero diagramma

axs[1].plot(x, y2, color='red', label='cos(x)')
axs[1].set_title('Subplot 2')
# label tou cos(x)
axs[1].legend()
plt.tight_layout()
plt.show()
