from math import *

cache = dict()



def isprime(p):
    for n in range(2,isqrt(p)+1):
        if p % n == 0:
            return False
    return True

def prevprime(p):
    p -= 1
    while isprime(p) == False:
        p -= 1
    return p


print(prevprime(13))

def b(n, p = None):
    if p == None:
        p = n

    if (n, p) in cache:
        return cache[(n,p)]

    if p == 2:
        # If n is even, return 1, else return 0.
        retVal = 1 - (n % 2)

    elif isprime(p):
        retVal = sum(( b(n - k * p, prevprime(p) ) for k in range(0, 1 + n//p)) )
    else:
        retVal = b(n, prevprime(p))

    cache[(n, p)] = retVal
    return retVal

print( "b(100) = " + str(b(100)) )
print( "b(200) = " + str(b(200)) )
for k in range(5, 73):
    print( "b(" + str(k) + ") = " + str(b(k)) )