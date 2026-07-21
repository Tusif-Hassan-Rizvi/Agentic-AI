a=10  #global variable

def something():

    print(globals()['a'])
    globals()['a']=20 #change global variable value
    a=26  #local variable
    print("inside function: ", a)

something()

print("outside value: ", a)
