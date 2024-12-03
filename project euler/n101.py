import math
def genpolyterms(polynomial,n):
	terms = []
	for term in range(1,n+1):
		t = 0
		for term2 in polynomial:
			t += term2[0]*term**term2[1]
		terms.append(t)
	return terms

def derivative(sequence):
	newseq = []
	for i in range(1,len(sequence)):
		newseq.append(sequence[i]-sequence[i-1])
	return newseq


def approx(sequence):
	degree = 0
	while sequence[0] != sequence[-1]:
		degree += 1
		sequence = derivative(sequence)
	return [(sequence[0]/math.factorial(degree)),degree]

def subtractsequence(sequence,polynomial):
	seq= [sequence[s]-(polynomial[0]*((s+1)**polynomial[1])) for s in range(len(sequence))]
	return seq

def findFIT(poly,approx):
	polyterms = genpolyterms(poly,100)
	approxterms = genpolyterms(approx,100)
	for i in zip(polyterms,approxterms):
		if i[0] != i[1]:
			return i[0]

def polynomial(sequence):
	BOP = []
	while sequence[0] != sequence[-1]:
		polynomial = approx(sequence)
		BOP.append(polynomial)
		sequence = subtractsequence(sequence,approx(sequence))
	BOP.append([sequence[0],0])
	return BOP

def remove0terms(poly):
	return [p for p in poly if p[0] != 0]

deg10poly = [[1,10],[-1,9],[1,8],[-1,7],[1,6],[-1,5],[1,4],[-1,3],[1,2],[-1,1],[1,0]]
#deg10poly = [[1,3]]
truepolynomial = genpolyterms(deg10poly,100)
BOP = [[1,0]]
k = 2
sumfits = 0
while BOP != deg10poly:
	fit = findFIT(BOP,deg10poly)
	print(fit)
	sumfits += fit
	BOP = polynomial(truepolynomial[:k])
	BOP = remove0terms(BOP)
	print(BOP)
	k += 1
print(sumfits) # VERY PROUD OF THIS ONE

