def add(a,b):
    return a+b

def sub(a,b):
    if b>a:
        a,b=b,a
    return a-b    

if __name__=="__main__":
    print(add(1,2))
    print(sub(2,4))
