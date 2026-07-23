import sys 
from time import sleep

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

count=1

def printname():
    global count
    print("Tusif: ", count)
    count+=1
    sleep(0.2)
    printname()


# printname()    


number=1
def print100():
    global number
    if number>10:
        return
    print("number: ",number)
    number+=1
    print100()  
print100()    