
import numpy as np
import matplotlib.pyplot as plt

# Define the function f(ω) as given
def f(ω):
    return np.cos((23 * ω) / 35000) - (2/14) * np.cos((11* ω) / 35000)

# Generate a range of ω values for plotting
ω_values = np.linspace(0, 5000, 500000)  # Use a dense range to get a smooth plot
f_values = f(ω_values)

# Plot the function
plt.figure(figsize=(10, 5))
plt.plot(ω_values, f_values, label="f(ω)")
plt.title("Plot of f(ω)")
plt.xlabel("ω (rad/s)")
plt.ylabel("f(ω)")
plt.grid(True)
plt.axhline(0, color='black', lw=0.5)
plt.legend()
plt.show()

# Find zeros of the function without using bisect
# Here we look for sign changes in the function values
sign_changes = np.where(np.diff(np.sign(f_values)))[0]
roots = ω_values[sign_changes]

# Print the roots
print(f"Roots found without using bisect: {roots / (2 * np.pi)} Hz") # Convert rad/s to Hz

