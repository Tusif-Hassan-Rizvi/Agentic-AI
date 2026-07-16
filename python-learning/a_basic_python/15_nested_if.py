num=input("Enter the number: ")
salary=500

num=int(num)

if num%2==0:
    print("Even")
    if(salary>=5000):
        print("great job")
    else: 
        print("not great")    
else:
    print("Odd")