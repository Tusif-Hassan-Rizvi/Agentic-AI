# List: A collection of values  


nums=[23, 55, 66, 22, 22]
names=["Tausif", "Tanwir", "Tanzil"]
mix=[nums, names]

print(nums)

print(nums[-1])
print(nums[2:4])
print(nums[2:])

mix=[nums, names]

print(mix)
print(len(mix))
print(mix[1][2])

combine=nums + names


print(combine)

# apend function 

nums.append(1053)

print(nums)

print(nums.count(1053))
print(nums.count(22))

# insert specific place 

nums.insert(0,2522)

print(nums)


# remove value 

nums.remove(1053)
print(nums)


# remove index 

nums.pop(0)
print(nums)

# remove list value in range 

del nums[2:4]
print(nums)

# insert multiple value 

nums.extend([90,89, 2000, 23])

print(nums)


# replace list value 

nums[2:3]=[567,657]

print(nums)

# revers list 

nums.reverse()

print(nums)

# list sort function 

nums.sort()

print(nums)

# min and max function 

print(min(nums))
print(max(nums))