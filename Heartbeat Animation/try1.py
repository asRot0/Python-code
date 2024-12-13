import numpy as np
import matplotlib.pyplot as plt

# Function to define the heart shape
def heart_shape(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

# Time array for heart shape
t = np.linspace(0, 2 * np.pi, 1000)
x, y = heart_shape(t)

# Plot the heart
plt.figure(figsize=(6, 6))
plt.plot(x, y, color='pink', lw=2)
plt.axis('equal')
plt.axis('off')
plt.show()