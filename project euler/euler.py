from math import *


def sumdivs(num):
	total = 1
	for i in range(2,isqrt(num)):
		if num % i == 0:
			total += i + (num // i)
	return total

def isPrime(num):
	for i in range(2,isqrt(num)+1):
		if num % i == 0:
			return False
	return True

