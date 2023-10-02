# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:23:42 2023

@author: Admin
"""

import h5py
import numpy as np
import matplotlib.pyplot as plt

# Open the HDF5 file in read mode
h5file = h5py.File('ECOSTRESS_L2_LSTE_29372_034_20230910T205241_0601_01.h5', 'r')

# Get a list of dataset names within the HDF5 file
dataset_names = 'SDS/Emis1_err'

#we found that by encountering an eror in MATLAB, searching for it, 
#which showed that the datasets are more than we exoected, so found the 
#names and the paths to to them and here we are.

# Replace 'your_dataset' with the actual dataset name in your HDF5 file
data = h5file[dataset_names][:]
print(data)


# Close the HDF5 file when you're done reading data
h5file.close()

# Compute the FFT of the data
fft_result = np.fft.fft(data)

# If you want to compute the frequencies corresponding to the FFT result, you can use np.fft.fftfreq:
sampling_rate = 1000  # Replace with your actual sampling rate (in Hz)
freqs = np.fft.fftfreq(len(data), 1/sampling_rate)

# You can get the magnitude of the FFT result using np.abs
magnitude = np.abs(fft_result)

# Plot the magnitude spectrum
plt.figure(figsize=(10, 6))
plt.plot(freqs, magnitude)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('FFT Magnitude Spectrum')
plt.grid(True)
plt.show()