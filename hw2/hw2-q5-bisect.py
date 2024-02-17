from scipy.optimize import bisect
import numpy as np

c = 35000
def formant_frequency(l1, l2, A1, A2, c):
    r1 = (A2 - A1) / (A2 + A1)
    def equation(omega):
        tau1 = l1 / c
        tau2 = l2 / c
        return np.cos(omega * (tau1 + tau2)) + r1 * np.cos(omega * (-tau1 + tau2))

    # bisection method (0~5000 rad/sec)
    omega_guess = bisect(equation, 0, 5000)
    
    # formant frequency -> Hz conversion
    f_formant = omega_guess / (2 * np.pi)
    return f_formant

vowels = {
    'i': {'l1': 9, 'l2': 6, 'A1': 8, 'A2': 1},
    'ae': {'l1': 9, 'l2': 18, 'A1': 1, 'A2': 8},
    'a': {'l1': 9, 'l2': 13, 'A1': 7, 'A2': 2},
    'N': {'l1': 17, 'l2': 6, 'A1': 8, 'A2': 6},
}
formant_frequencies = {}
for vowel, params in vowels.items():
    formant_frequencies[vowel] = formant_frequency(
        params['l1'], params['l2'], params['A1'], params['A2'], c
    )
print(formant_frequencies)