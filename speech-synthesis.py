import scipy
import numpy as np

# Define the sampling rate and fundamental frequencies for a boy and a girl
sampling_rate = 8000  # Common sampling rate for speech processing
f0_boy = 120  # Fundamental frequency for a boy
f0_girl = 220  # Fundamental frequency for a girl
duration = 2  # same duration as 'Ah' sound.

# Choose a fundamental frequency to synthesize the vowel, let's use the boy's frequency
f0 = f0_boy

# Generate a harmonic series up to 4000 Hz
harmonics = np.arange(f0, 4000, f0)

# Generate the time vector
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Create a signal by summing harmonics
signal = sum(np.sin(2 * np.pi * harmonic * t) for harmonic in harmonics)

# Define formant frequencies for filtering
formants = [800, 1600, 3000]

# Create bandpass filters for each formant frequency
filtered_signal = signal
for formant_freq in formants:
    # Design a bandpass filter around the formant frequency
    b, a = scipy.signal.butter(N=2, Wn=[(formant_freq - 100)/(sampling_rate/2), 
                           (formant_freq + 100)/(sampling_rate/2)], btype='band')
    # Apply the filter to the signal
    filtered_signal = scipy.signal.lfilter(b, a, filtered_signal)

# Normalize the filtered signal
filtered_signal /= np.max(np.abs(filtered_signal))

# Convert to 16-bit PCM format for WAV file
filtered_signal_int16 = np.int16(filtered_signal * 32767)

# Save the synthesized vowel signal as a .wav file
output_wav_path = 'synthesized_vowel.wav'
scipy.io.wavfile.write(output_wav_path, sampling_rate, filtered_signal_int16)