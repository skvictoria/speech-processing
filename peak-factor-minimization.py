'''
Implement the paper "Peak factor minimization using a time-frequency domain swapping algorithm"
written by Edwin van der ouderaa et al.
'''
import numpy as np

def generate_multisine(A, phi, N, T):
    t = np.arange(N) * T
    f = np.zeros_like(t)
    for i in range(len(A)):
        f += A[i] * np.cos(2 * np.pi * i * t / T + phi[i])
    return f

def time_frequency_swap_algorithm(A, phi, N, T, clipping_ratio=0.85):
    # Generate the initial multisine signal
    f = generate_multisine(A, phi, N, T)
    
    # Initialize variables
    Kr_previous = float('inf')  # Initialize to infinity for the first iteration
    iteration = 0

    # Start the algorithm loop
    while True:
        # Perform the FFT
        F = np.fft.fft(f)
        
        # Retain the phases and impose the original magnitudes
        # to get a symmetric magnitude spectrum and anti-symmetric phase spectrum
        F_magnitude = np.abs(F)
        F_phase = np.angle(F)
        F_magnitude[:N//2] = A[:N//2]  # Impose original magnitudes for the positive frequencies
        F_magnitude[N//2:] = A[:N//2][::-1]  # Ensure symmetric magnitude spectrum
        
        # Rebuild the Fourier spectrum with the original magnitudes and retained phases
        F = F_magnitude * np.exp(1j * F_phase)
        
        # Perform the inverse FFT
        f = np.fft.ifft(F).real
        
        # Clip the time signal
        max_val = np.max(np.abs(f))
        clip_val = max_val * clipping_ratio
        f_clipped = np.clip(f, -clip_val, clip_val)
        
        # Recalculate the effective energy E_eff using the clipped signal
        E_eff = np.sqrt(np.mean(f_clipped**2))

        # Calculate the new Kr
        M_plus = np.max(f_clipped)
        M_minus = np.min(f_clipped)
        Kr = (M_plus - M_minus) / (2 * E_eff)
        
        # Increment iteration count
        iteration += 1
        
        # Check for convergence: exit loop if Kr no longer diminishes
        if Kr >= Kr_previous:
            break
        Kr_previous = Kr  # Update the previous Kr for the next iteration
    
    return f_clipped, Kr, iteration

def time_frequency_swap_algorithm_E_constant(A, phi, N, T, clipping_ratio=0.85):
    # Generate the initial multisine signal
    f = generate_multisine(A, phi, N, T)
    
    # Initialize variables
    Kr_previous = float('inf')  # Initialize to infinity for the first iteration
    iteration = 0
    
    # Calculate the effective energy using the amplitudes
    E_eff = np.sqrt(np.sum(np.array(A)**2) / 2)

    # Start the algorithm loop
    while True:
        # Perform the FFT
        F = np.fft.fft(f)
        
        # Retain the phases and impose the original magnitudes
        # to get a symmetric magnitude spectrum and anti-symmetric phase spectrum
        F_magnitude = np.abs(F)
        F_phase = np.angle(F)
        F_magnitude[:N//2] = A[:N//2]  # Impose original magnitudes for the positive frequencies
        F_magnitude[N//2:] = A[:N//2][::-1]  # Ensure symmetric magnitude spectrum
        
        # Rebuild the Fourier spectrum with the original magnitudes and retained phases
        F = F_magnitude * np.exp(1j * F_phase)
        
        # Perform the inverse FFT
        f = np.fft.ifft(F).real
        
        # Clip the time signal
        max_val = np.max(np.abs(f))
        clip_val = max_val * clipping_ratio
        f_clipped = np.clip(f, -clip_val, clip_val)
        
        # Calculate the new Kr
        M_plus = np.max(f_clipped)
        M_minus = np.min(f_clipped)
        Kr = (M_plus - M_minus) / (2 * E_eff)
        
        # Increment iteration count
        iteration += 1
        
        # Check for convergence: exit loop if Kr no longer diminishes
        if Kr >= Kr_previous:
            break
        Kr_previous = Kr  # Update the previous Kr for the next iteration
    
    return f_clipped, Kr, iteration

# Parameters for the multisine signal
N = 1000  # Number of samples
T = 1/N  # Sampling period
A = [1] * (N//2)  # Amplitudes of the harmonics (flat spectrum)
phi = [0] * (N//2)  # Initial phases of the harmonics

# Run the algorithm
f_compressed, final_Kr, total_iterations = time_frequency_swap_algorithm(A, phi, N, T)

print(f"Final Kr: {final_Kr}, Total Iterations: {total_iterations}")
