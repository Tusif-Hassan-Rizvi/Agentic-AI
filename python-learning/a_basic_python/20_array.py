from array import *


arr1=array('i',[23, 55,62,22,2523])

print(type(arr1))

print(arr1.tolist())

for value in arr1:
    print(value)



# get buffer info of array     

print(arr1.buffer_info())