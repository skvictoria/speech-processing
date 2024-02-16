import numpy as np
from scipy.io import wavfile
import librosa
import librosa.display

# load the wav file
fs, signal = wavfile.read('data/e-v.wav')

# convert to mono if the signal is stereo
if signal.ndim > 1:
    signal = signal.mean(axis=1)

# normalize the signal to float, by dividing into max(int16)
signal = signal / np.iinfo(np.int16).max

# get amplitude/phase by FFT
F = np.fft.fft(signal)
amplitudes = np.abs(F)
phases = np.angle(F)

# Get spectrogram by calculating STFT (using librosa.stft library)
D = np.abs(librosa.stft(signal, n_fft=1024, hop_length=512))

# get the most 8-strongest frequency
num_formants = 8
mean_spectrum = np.mean(D, axis=1)
peak_indices = np.argsort(mean_spectrum)[-num_formants:]

# formant frequency (From spectrogram)
formant_frequencies = peak_indices * fs / 1024
# formant phase (From fft result)
formant_phases = phases[peak_indices]

# Generate sine wave
synthesized_signal_formants = np.zeros_like(signal)
time_vector = np.arange(signal.size) / fs
for i, freq in enumerate(formant_frequencies):
    amplitude = amplitudes[peak_indices[i]]
    phase = formant_phases[i]
    # fine-tune with the amplitude and phase from FFT result
    synthesized_signal_formants += amplitude * np.cos(2 * np.pi * freq * time_vector + phase)

# normalized
synthesized_signal_formants = synthesized_signal_formants / np.max(np.abs(synthesized_signal_formants))

# convert to int16 (to save the file)
synthesized_signal_formants_int16 = np.int16(synthesized_signal_formants * np.iinfo(np.int16).max)

# save wav file
output_file_path_formants = 'synthesized_formants_e-v.wav'
wavfile.write(output_file_path_formants, fs, synthesized_signal_formants_int16)