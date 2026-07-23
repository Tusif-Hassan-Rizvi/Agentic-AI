nums=[23,353,62,66,0,33,5]


# evens=[]
# odds=[]


# for i in nums:
#     if i%2==0:
#         evens.append(i)
#     else:
#         odds.append(i)

# print(odds)       


# def is_even(n):
#     return n%2==0

# lamda function with filter
evens=list(filter(lambda n: n%2==0, nums))
print(evens) 


# Write a Python program using the filter
# function and a lambda expression
# to extract all the numbers greater
# than 50 from a given list.


# Example list
example_list=[10, 55, 32, 75, 90, 41, 68]


greter_fifty=list(filter(lambda n: n>50, example_list))

print(greter_fifty)


