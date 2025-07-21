import numpy as np
from scipy.fft import fft, fftfreq


def compute_fft_all_channels(data, sampling_rate_hz=40000):
    """
    data: numpy array of shape (n_channels, n_samples)
    sampling_rate_hz: sampling frequency in Hz
    """
    print("Starting Fourier Transformations")
    n_channels, n_samples = data.shape
    freqs = fftfreq(n_samples, d=1/sampling_rate_hz)
    fft_data = np.zeros((n_channels, n_samples), dtype=np.complex64)

    for ch in range(n_channels):
        fft_data[ch] = fft(data[ch])

    return freqs, fft_data