import numpy as np

# This program is an example only

# Reading .npz files
data = np.load('SeBn\\B=16.npz')

# Get all array names in the file
print(data.files)

# Read one of the arrays
array_name = 'z'
my_array = data[array_name]
print(my_array)

# multiple arrays in the file
for array_name in data.files:
    print(f'Array name: {array_name}')
    print(data[array_name])
