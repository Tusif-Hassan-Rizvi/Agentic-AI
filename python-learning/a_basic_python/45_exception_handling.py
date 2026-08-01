# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

print("Resource open successfully")


try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    result=a/b
    print("Result is : ", result)

except ZeroDivisionError as ze:
   print("An error occured: ", ze)
except ValueError as ve:
   print("An error occured, by wrong value enter",ve)   
except Exception as e:
  print("Something went wrong!", e)

finally:   
    print("Resources closed.")


# either we need except block or finally with try block 

print("End of program")