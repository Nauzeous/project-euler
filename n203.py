from math import *
from euler import isPrime
squareprimes = [i**2 for i in range(2,10000) if isPrime(i)]

def NcR(n,r):
	top = factorial(n)
	bot = factorial(r)*factorial(n-r)
	return top/bot

def sqfree(num):
	for squareprime in squareprimes:
		if num % squareprime == 0:
			return False
	return True

def sqfreerowsum(n):
	row = [NcR(n,r) for r in range(1,n) if sqfree(NcR(n,r))]
	return row


sqfrees = [1]
for row in range(1,51):
	sqfrees.extend(sqfreerowsum(row))
sqfrees = set(sqfrees)
print(sum(sqfrees))