def greater_first(func):
    def wrap(a,b):
        if a<b:
         a,b=b,a
        return func(a,b)
    return wrap   




# moder way 
@greater_first
def sub(a,b):
    return a-b

@greater_first
def divide(a,b):
    return a/b


# old way to make use decorator
sub=greater_first(sub)
divide=greater_first(divide)


print(divide(4,2))
print(sub(4,2))
