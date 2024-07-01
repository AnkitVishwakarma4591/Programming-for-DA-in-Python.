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
print(var)

var = np.array([1,2,3,4,5],dtype=str)
var

# in numpy we access any elements using index.

print(var[0])

# Some basic command of numpy
var1 = np.array([1,2,3,4,5,6,7,8,9])
var1.reshape(3,3)

a = np.zeros((3,3),dtype=int)
b = np.ones(10)
c = np.full(5,10,dtype=int)
d = np.arange(1,20,2,dtype=float)
e = np.identity(5)
f = np.random.rand(10)       
f = np.random.randint(4,5) 
