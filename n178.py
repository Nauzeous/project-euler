

def sieve(n):
	primes = [True for i in range(n+1)]

	for p in range(2,n+1):
		if primes[p]:
			for j in range(p*p,n+1,p):
				primes[j] = False

	return [p for p in range(2,n) if primes[p]]

def numfactors(n):
	prod = 1
	for p in primes:
		exp = 0
		while n % p == 0:
			n /= p
			exp+=1
		prod *= (exp+1)
		if p > n:break
	return prod


primes = sieve(5_000_000)
print(len(primes))
nextn = 2
for i in range(2,10_000_000):
	currn = nextn
	nextn = numfactors(i+1)
	if currn == nextn:
		print(i,i+1)


