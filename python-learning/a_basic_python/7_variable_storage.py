a = 5
b = 5

# Get the memory address of variable 'a'
print(id(a))

# Everything in Python is an object
print(id(b))

# Both variables 'a' and 'b' refer to the same object (5) and share the same memory address.


# string interning 

name="My name is Tausif"
name2="My name is Tausif"

print(id(name))
print(id(name2))