from array import *


arr1=array('i',[23, 55,62,22,2523])

arr1.append(77)

arr1.reverse()


# copy array and create new array 
# arr2=array(arr1.typecode, arr1.tolist())

# more mermory efficient code for copy array 

arr2=array(arr1.typecode, (n for n in arr1))

print("arr2 value: ",arr2)
for value in arr1:
    print(value)


