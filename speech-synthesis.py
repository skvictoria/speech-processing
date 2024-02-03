import numpy as np
from scipy.signal import lfilter
from scipy.io.wavfile import write

f0 = 120  # Fundamental frequency (Hz)

# # Define the sampling rate and the poles for the formants
sampling_rate = 8000  # in Hz
formant_frequencies = [800, 1600, 3000]  # in Hz
duration = 2.0  # signal duration in seconds

p1_radius = 0.9
p2_radius = 0.8
p3_radius = 0.8
p1_angle = 2 * np.pi * formant_frequencies[0] / sampling_rate
p2_angle = 2 * np.pi * formant_frequencies[1] / sampling_rate
p3_angle = 2 * np.pi * formant_frequencies[2] / sampling_rate

# Calculate the poles for each formant frequency
p1 = p1_radius * np.exp(1j * p1_angle)
p2 = p2_radius * np.exp(1j * p2_angle)
p3 = p3_radius * np.exp(1j * p3_angle)

# Poles must come in conjugate pairs for a real filter
poles = [p1, np.conj(p1), p2, np.conj(p2), p3, np.conj(p3)]

# Generate the filter coefficients from the poles
a = np.poly(poles)

# Generate the source signal: sum of harmonics based on the fundamental frequency f0
harmonics = np.arange(0, 4000, f0)
source_signal = np.zeros(int(sampling_rate * duration))

t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Sum sinusoids at the fundamental frequency and its harmonics
for harmonic in harmonics:
    source_signal += np.sin(2 * np.pi * harmonic * t)

# Normalize the source signal
source_signal /= np.max(np.abs(source_signal))

# Filter the source signal to synthesize the vowel sound
synthesized_vowel = lfilter([1], a, source_signal)

# Normalize the synthesized vowel signal to prevent clipping
synthesized_vowel /= np.max(np.abs(synthesized_vowel))

# Convert to 16-bit PCM format for WAV file
synthesized_vowel_int16 = np.int16(synthesized_vowel * 32767)

# Save the synthesized vowel signal as a .wav file
output_wav_path_full = 'synthesized_vowel_full.wav'
write(output_wav_path_full, sampling_rate, synthesized_vowel_int16)