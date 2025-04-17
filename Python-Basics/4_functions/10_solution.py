def fact(n):
    if n==0:
        return 1
    else:
        fac=n*fact(n-1)
        return fac
    
print(fact(5))