def factorial(n):
    if n==1 or n==0:
        return 1
    fact=1
    while(n>=1):
        fact=fact*n
        n=n-1
    return fact      



print(factorial(12))
        