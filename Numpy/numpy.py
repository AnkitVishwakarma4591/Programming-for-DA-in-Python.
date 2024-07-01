# importing python library numpy
import numpy as np

# use of numpy arrays
# To store multiple data in a array
# Collection of homegenous data.
# numpy array are much faster than list ,tuple,dictionary or set

#  How to create a numpy array 
var = np.array([1,2,3,4,5])
print(var)

# checking the type of array
type(var)

# changing the datatype of array
var = np.array([1,2,3,4,5],dtype=float)
var = np.array([1,2,3,4,5],dtype=str)
print(var)