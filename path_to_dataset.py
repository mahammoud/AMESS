# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:19:33 2023

@author: Admin
"""

import h5py

# Open the HDF5 file in read mode
h5file = h5py.File('ECOSTRESS_L2_LSTE_29372_034_20230910T205241_0601_01.h5', 'r')

# Function to recursively traverse and print all datasets and their paths
def print_datasets(name, obj):
    if isinstance(obj, h5py.Dataset):
        print(f"Dataset Name: {name}, Path: {obj.name}")

# Iterate through the HDF5 file to list datasets and their paths
h5file.visititems(print_datasets)

# Close the HDF5 file
h5file.close()