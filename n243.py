import math
def sieve(n):
	primes = [True for i in range(n+1)]

	for i in range(2,n):
		if primes[i]:
			for p in range(i*i,n,i):
				primes[p] = False

	return [a for a in range(2,n) if primes[a]]


def phi(n):
	r = n
	for i in range(2,math.isqrt(n)+1):
		if n % i == 0:
			r -= r / i
			while n % i == 0:
				n /= i
   
	if (n > 1):
		r -= r / n;
	return r



primes = sieve(100)
num = 1

def compositephi(i):
	num = 1
	for j in range(i+1):
		num *= (primes[j]-1)
	return num

bmark = 15499/94744

print(bmark)
print(2*3*5*7*11*13*17*19*23)

n = 223092870

ratio = 1
while ratio > 15499/94744:
	n+=1
	x = phi(n)
	ratio = x / (n-1)

print("done")

