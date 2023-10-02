# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:30:34 2023

@author: Admin
"""

import h5py
import matplotlib.pyplot as plt

# Open the HDF5 file in read mode
h5file = h5py.File('ECOSTRESS_L2_LSTE_29372_034_20230910T205241_0601_01.h5', 'r')

# Replace 'your_dataset_name' with the actual dataset name
dataset_name = 'SDS/Emis2_err'

# Access the dataset
dataset = h5file[dataset_name]

# Read the data
data = dataset[:]

# Close the HDF5 file
h5file.close()

# Plot the data
plt.figure(figsize=(8, 6))  # Set the figure size (optional)
plt.imshow(data, cmap='viridis')  # Change the colormap as needed
plt.colorbar()  # Add a colorbar (optional)
plt.title('Your Data Visualization')  # Add a title (optional)
plt.show()