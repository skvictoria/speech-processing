import numpy as np
import matplotlib.pyplot as plt

# Define the continuous time signal x(t)
def x_t(t):
    return 2 * np.cos(200 * np.pi * t + 0.25 * np.pi) - np.sin(300 * np.pi * t + 0.5 * np.pi)

# Sampling
Fs = 1080  # Sampling frequency
T = 1/Fs  # Sampling period
N = Fs  # Number of points (1 second worth of samples)
t = np.arange(0, 1, T)  # Time vector for one second
x_n = x_t(t)  # Sampled signal

# Perform DFT
X_k = np.fft.fft(x_n)

# Frequencies
freqs = np.fft.fftfreq(N, T)

# Problem A (b): Plot the magnitude spectrum
plt.figure(figsize=(12, 6))
plt.stem(freqs[:N // 2], np.abs(X_k[:N // 2]), 'b', markerfmt=" ", basefmt="-b")
plt.title('Magnitude Spectrum of x[n]')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude |X(k)|')
plt.grid(True)
plt.show()

# Results for Problem A (b)
# We return the first few DFT coefficients and their corresponding frequencies for comparison
dft_results = [(freq, coeff) for freq, coeff in zip(freqs[:N // 2], X_k[:N // 2])]
print(dft_results[100], dft_results[150])