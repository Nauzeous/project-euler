from euler import *

primes = [i for i in range(2,7100) if isPrime(i)]

sqprimes = [p**2 for p in primes]
cubprimes = [p**3 for p in primes[:73]]
fourprimes = [p**4 for p in primes[:23]]
total = 0
numbers = []
for prime1 in sqprimes:
	for prime2 in cubprimes:
		for prime3 in fourprimes:
			num = prime1 + prime2 + prime3
			if num < 50_000_000:
				numbers.append(num)
				total += 1

rnumbers = set(numbers)
print(len(rnumbers))
