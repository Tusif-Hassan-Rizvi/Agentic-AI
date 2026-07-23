def factorial(n):
    if n==0 or n==1:
        return 1

    return n * factorial(n-1)


print(factorial(10))    


def fact (n) :
    if n == 0:
      return 0
    return n * fact(n - 1)
res = fact(4)
print(res)