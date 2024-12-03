import numpy as np


def sieve(n):
	primes = [True for i in range(n+1)]

	for p in range(2,n+1):
		if primes[p]:
			for j in range(p*p,n+1,p):
				primes[j] = False

	return [p for p in range(2,n) if primes[p]]

ps = sieve(8_000_000)
lps = np.log10(ps)

pfs = [1] 

weights = [lps[0]*2]

for _ in range(500499):
    # Find minimum weight index
    mi = np.argmin(weights)
    m = weights[mi]
    
    # Check if we need to expand
    wrap = lps[len(pfs)]
    
    if wrap < m:
        # Expand arrays
        pfs += [1]
        weights = np.pad(weights, (0, 1), mode='constant', constant_values=wrap*2)
    else:
        # Update existing entry
        pfs[mi] += (pfs[mi]+1)
        weights[mi] = lps[mi] * (pfs[mi] + 1)

MOD = 500500507

total = 1

print(pfs)

for a,b in zip(ps,pfs):
	total *= pow(a,b,MOD)
	total = total % MOD

print(total)










