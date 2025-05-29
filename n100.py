from math import sqrt

def possiblex(x):
	root2 = 1.4142135623730950488
	bdiscs = (root2*x)//2
	ratio = bdiscs*(bdiscs-1)/(x*(x-1))
	while ratio < 0.5:
		bdiscs += 1
		ratio = bdiscs*(bdiscs-1)/(x*(x-1))
		if ratio*20 == 10:
			print(bdiscs,x)
 # 1000000002604 works

discs = 1_000_000_000_000
solfound = False
for i in range(10**12,3*10**12):
	if (possiblex(i)):break
