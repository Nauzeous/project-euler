# proud of this one, used matrices to produce A(2^m,2^n) and worked from there

fib = [0,1,1,2]

for i in range(50):
	fib.append(fib[-1]+fib[-2])

MOD = 1123581313

def matsquare(a,b,c,d):
	global MOD
	p = a*a+b*c
	q = a*b+b*d
	r = c*a+d*c
	s = c*b+d*d
	return p%MOD,q%MOD,r%MOD,s%MOD

def matmul(a,b,c,d,e,f,g,h):
	global MOD
	p = a*e+b*g
	q = a*f+b*h
	r = c*e+d*g
	s = c*f+d*h
	return p%MOD,q%MOD,r%MOD,s%MOD

def A(i,j):
	global matlist1,matlist2
	startmat = 1,0,0,1
	g = [int(x) for x in str(bin(j))[:1:-1]]
	# vertical component first
	for power2,n in enumerate(g):
		if n == 1:
			startmat = matmul(*matlist1[power2],*startmat)
	a,b = startmat[3]-startmat[2],startmat[2]	
	startmat = 1,0,0,1
	g = [int(x) for x in str(bin(i))[:1:-1]]
	for power2,n in enumerate(g):
		if n == 1:
			startmat = matmul(*matlist2[power2],*startmat)

	c,d = startmat[0]*a+startmat[1]*b,startmat[2]*a+startmat[3]*b

	print(d)
	return d

a,b,c,d = -1,1,1,2
matlist1 = []
for i in range(40):
	matlist1.append([a,b,c,d])
	a,b,c,d = matsquare(a,b,c,d)

a,b,c,d = 2,3,1,1
matlist2 = []
for i in range(40):
	matlist2.append([a,b,c,d])
	a,b,c,d = matsquare(a,b,c,d)

tot = 0
sval = 50
for i in range(2,sval+1):
	for j in range(2,sval+1):
		tot += A(fib[i],fib[j])
print(tot%MOD)