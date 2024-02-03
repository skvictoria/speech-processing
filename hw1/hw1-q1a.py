import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-0.01, 0.01, 1000)
x_t= 3*np.cos(300*np.pi*t + 0.1*np.pi)- 2*np.cos(600*np.pi*t + 0.2*np.pi) +np.cos(900*np.pi*t +0.3*np.pi)
# Plot y(t)
plt.figure(figsize=(12, 6))
plt.plot(t, x_t)  # Convert time to milliseconds for plotting
plt.title('Continuous-time Signal x(t)')
plt.xlabel('Time (s)')
plt.ylabel('x(t)')
plt.grid(True)
plt.show()
