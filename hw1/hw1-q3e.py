import numpy as np
import matplotlib.pyplot as plt
    
def non_ideal_pulse(t):
    # Define conditions for different parts of the pulse
    condition_plus = (t >= -2 * 0.001) & (t <= 0)
    condition_minus = (t <= 0.2 * 0.001) & (t >= 0)
    
    # Use np.where to apply the conditions to the whole array
    # For the positive slope part of the pulse
    pulse_plus = np.where(condition_plus, t/2+1, 0)
    # For the negative slope part of the pulse
    pulse_minus = np.where(condition_minus, -t/2+1, 0)
    
    # Combine both parts
    return pulse_plus + pulse_minus

# Define the sampling rate and sampling period
sampling_rate = 500  # in Hz
T = 1 / sampling_rate  # Sampling period in seconds

# Define n values and calculate x[n] values
n_values = np.array([0, 1, 2, 3, 4, 5], dtype=float)
x_n_values = n_values / (2 ** (n_values - 3))

# Define a time range for plotting
t_range = np.linspace(-0.03, 0.03, 1000)  # -10ms to 30ms

# Initialize y(t) as a zero array
y_t = np.zeros_like(t_range)

# Calculate the contribution to y(t) for each sample in x[n]
for n, x_n in zip(n_values, x_n_values):
    # Subtract n*T from t_range and scale by the sampling rate to get the correct argument for np.sinc
    y_t += x_n * non_ideal_pulse(t_range-n*T)

# Plot y(t)
plt.figure(figsize=(12, 6))
plt.plot(t_range * 1000, y_t)  # Convert time to milliseconds for plotting
plt.title('Continuous-time Signal y(t) from D-to-C Conversion')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude y(t)')
plt.grid(True)
plt.show()
