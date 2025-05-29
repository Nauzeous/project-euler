from math import factorial as fct

def B(n):
	product = 1
	factn = fct(n)

	for r in range(1,n//2 + 1):
		ncr = ((factn)//(fct(r)*fct(n-r)))
		print(ncr,n,r)
		product *= ncr
	return product ** 2

print(B(5))