# def num(num1=0, num2=0):
#     return num1+num2


# print(num(1,3))
# print(num(1))


# variable length arguments 
def num(num1, *num2):
    print(num1, num2)
    sum=num1
    for n in num2:
        sum +=n
    print("this is sum", sum)    
    return 0


result=num(3,5,35,6)



# keyword argument 
def person(name, age):
    print("Person name is: ", name)
    print("Person age is: ", age)


person( age=26, name="Tausif")    



def profile(name, **other):
    print("name and other details", name, other)

    for k, v in other.items():
        print(k, ":", v)


profile(name="Tausif", age=26, title="Frontend Developer", salary=100, skill=["HTML", "CSS", "JS", "React", "Javascript"])    