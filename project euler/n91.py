
def dotvec(a,b):
	return (a[0]*b[0]+a[1]*b[1])

def vecsub(a,b):
	return [a[0]-b[0],a[1]-b[1]]

def isratriangle(p,q):
	pq = vecsub(p,q)
	return dotvec(q,pq) == 0 or dotvec(p,pq) == 0

sols = 0
sizegrid = 50
for a in range(0,sizegrid + 1):#Q >= P for all 
	for b in range(0,sizegrid + 1):
		if a + b == 0:
			continue
		for c in range(0,a + 1):
			for d in range(0,sizegrid + 1):
				if c + d == 0 or a == c and b == d:
					continue
				sols += isratriangle([a,b],[c,d])
print(sols)