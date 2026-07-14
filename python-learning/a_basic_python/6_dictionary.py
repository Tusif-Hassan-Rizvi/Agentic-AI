
# A dictionary is a built-in Python data structure used to store data in key:value pairs.

# Keys behave like sets (unique elements), and values behave like lists.
data = {'name': 'Tausif', 'age': 26, 'work': 'Frontend Developer'}

print(type(data))
print(data['age'])

# It returns an error if the key is not found
# print(data['22'])

# The get() method does not return an error if the key is not found
print(data.get('work'))

print(data.get(1))

print(data.get('rizvi', 'not found!'))

# Note: 'name' is duplicated here. In Python, duplicate keys are overwritten by the last occurrence.
data = {'name': 'Tausif', 'age': 26, 'work': 'Frontend Developer', 'name': 'Tausif'}

print(data)



# combine set and list in a dictionary 

# Predictable order using a list for keys
keys={"Tanzil", "Tausif", "Tanwir"}
values=[26, 25, 58]

combineDict = dict(zip(keys, values))
print(combineDict)  # Always maps Tausif to 25, Tanzil to 26, Tanwir to 58


# Nested Dictionaries (Dictionary inside a dictionary)

language = {
    'delhi': 'Hindi',
    'bihar': ['Hindi', 'Magahi', 'Bhojpuri', 'Maithili', 'Angika', 'Bajjika'],
    'biharLanguage': {
        'magadh': 'magahi',
        'mithila': 'maithili'
    }
}


print(language)
print(language['bihar'][0])
print(language['biharLanguage']['mithila'])