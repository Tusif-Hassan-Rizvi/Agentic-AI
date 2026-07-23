from functools import reduce

nums=[23,353,62,66,0,33,5]


evens=list(filter(lambda n: n%2==0, nums))
double_it=list(map(lambda n: n*2, evens))
sum=reduce(lambda a,b:a+b, double_it)

print("Evens", evens) 
print("Here is double it ", double_it)
print("sum: ", sum)

cube_list=[2,3,4]




sum_of_cube=reduce(lambda a,b:a+b, list(map(lambda n:n**3, cube_list)))

print("sum of cubes: ", sum_of_cube)