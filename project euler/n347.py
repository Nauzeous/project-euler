def getprimes(maxnum):
	primelist = []
	primes = [True for i in range(maxnum+1)]
	p = 2
	while p<maxnum:
		if primes[p]:
			primelist.append(p)
			for i in range(p*p,maxnum,p):
				primes[i] = False
		p += 1
	return primelist

print(getprimes(100))


def S(n):
	while primes[i] < n//2:
		while primes[j] < n//2:
			pass
