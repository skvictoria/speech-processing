import numpy as np
import matplotlib.pyplot as plt

# Define the impulse train y[n] with period of 25 samples
N_impulse = 25
y_n_100 = np.zeros(100)
y_n_120 = np.zeros(120)
y_n_100[::N_impulse] = 1
y_n_120[::N_impulse] = 1
Fs = 1080  # Sampling frequency
T = 1/Fs  # Sampling period

# Compute 100-point and 120-point DFT
Y_k_100 = np.fft.fft(y_n_100)
Y_k_120 = np.fft.fft(y_n_120)

# Frequencies for each DFT
freqs_100 = np.fft.fftfreq(100, T)
freqs_120 = np.fft.fftfreq(120, T)

# Plot the magnitude spectrum for 100-point DFT
plt.figure(figsize=(14, 7))
plt.subplot(2, 1, 1)
plt.stem(freqs_100, np.abs(Y_k_100), 'b', markerfmt=" ", basefmt="-b")
plt.title('100-Point DFT Magnitude Spectrum of y[n]')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude |Y(k)|')
plt.grid(True)

# Plot the magnitude spectrum for 120-point DFT
plt.subplot(2, 1, 2)
plt.stem(freqs_120, np.abs(Y_k_120), 'g', markerfmt=" ", basefmt="-g")
plt.title('120-Point DFT Magnitude Spectrum of y[n]')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude |Y(k)|')
plt.grid(True)

plt.tight_layout()
plt.show()
