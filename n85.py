from math import factorial


def ncr(n):
	top = factorial(n)
	bot = 2*factorial(n-2)
	return top/bot


def numrects(length,width):
	return ncr(length+1)*ncr(width+1)

bestcomb = []
best = 1_000_000
print(numrects(77,36))
l = 1
w = 1
for l in range(1,1_000_0):
	#print(l,bestcomb)
	for w in range(1,1_000_0):
		nrs = numrects(l,w)
		if nrs > 2_000_000 + best:
			break
		if abs(2_000_000 - nrs) < best:
			best = abs(2_000_000 - nrs)
			bestcomb = [l,w]
			break
print("hi")
print(bestcomb)