import math

def isdigitpower(n):
	sumdigits = sum([int(i) for i in str(n)])
	z = 1
	if sumdigits == 1:
		return False
	while z < n:
		z *= sumdigits
	return z == n

	
t = 1
i = 12
while t != 31:
	i += 1
	if isdigitpower(i):
		print(i,t)
		t += 1 

print(math.log2(4913)/math.log2(4+9+1+3))

#81 512 2401 4913 5832 17576 234256 390625 614656