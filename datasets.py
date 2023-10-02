# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:27:02 2023

@author: Admin
"""

import h5py

# Open the HDF5 file in read mode
h5file = h5py.File('ECOSTRESS_L2_LSTE_29372_034_20230910T205241_0601_01.h5', 'r')

# Get a list of dataset names within the HDF5 file
dataset_names = list(h5file.keys())

# Close the HDF5 file
h5file.close()

# Print the list of dataset names
for name in dataset_names:
    print(name)