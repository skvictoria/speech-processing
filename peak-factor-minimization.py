'''
Implemented the paper "Peak factor minimization using a time-frequency domain swapping algorithm"
'''
import scipy.io.wavfile as wav
import numpy as np

def time_frequency_swap_algorithm(signal, fs, clipping_ratio=0.85):
    # Generate the initial multisine signal
    N = len(signal)
    T = 1/fs
    f = signal.copy()
    
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

# load wav file
#file_path = 'e-v.wav'
file_path = 'xsignal.wav'
fs, data = wav.read(file_path)

# convert to mono if stereo
if len(data.shape) == 2:
    data = data.mean(axis=1)

f_compressed, final_Kr, total_iterations = time_frequency_swap_algorithm(data, fs)

print(f"Final Kr: {final_Kr}, Total Iterations: {total_iterations}")

# save wav file
#output_file_path = 'processed_e-v.wav'
output_file_path = 'processed_xsignal.wav'
wav.write(output_file_path, fs, f_compressed.astype(np.int16))