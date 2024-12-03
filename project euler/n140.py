import math

def isprime(n):
	for i in range(2,math.isqrt(n)):
		if n % i == 0:
			print(i, n // i)
			return False

	return True

print(isprime(6))