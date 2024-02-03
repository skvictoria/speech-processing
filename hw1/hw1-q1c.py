import numpy as np
import matplotlib.pyplot as plt

# Given values
fs = 1180  # Sampling rate in Hz
f1 = 300  # Frequency of the first cosine term
f2 = 600  # Frequency of the second cosine term
f3 = 900  # Frequency of the third cosine term

# Calculate the least common multiple (LCM) of the periods of the cosine components to find the fundamental period T0
T0_cont = 1/150 * 2 * np.pi  # Multiply by 2*pi to convert to radians

# Calculate the number of discrete samples that would occur in one period T0
num_samples = int(fs * T0_cont / (2 * np.pi))  # Convert T0_cont back to seconds

# Generate the discrete time array
n = np.arange(num_samples*2)

# Discrete-time signal x[n]
x_n = 3 * np.cos(2 * np.pi * f1 / fs * n + 0.1 * np.pi) \
      - 2 * np.cos(2 * np.pi * f2 / fs * n + 0.2 * np.pi) \
      + np.cos(2 * np.pi * f3 / fs * n + 0.3 * np.pi)

# Plot the discrete-time signal using stem plot
plt.stem(n, x_n, use_line_collection=True)
plt.title('Discrete-Time Signal x[n]')
plt.xlabel('Sample Number')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
