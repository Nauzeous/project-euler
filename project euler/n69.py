from euler import *

primes = []

for i in range(2,1000_000):
	if isPrime(i):
		primes.append(i)

def coPrime(a,b): # a > b
	i = 0
	while primes[i] <= b:
		if a % primes[i] == 0 and b % primes[i] == 0:
			return False
		i += 1
	return True


def phi(n):
	total = 1
	for i in range(2,n):
		if coPrime(n,i):
			total += 1
	return total
bestrat = 1

i = 0
n = primes[i]
while n < 1_000_000:
	print(n)
	if n > bestrat * phi(n):
		bestn = n
		bestrat = n/phi(n)
	i += 1
	n *= primes[i]

print(bestn)
