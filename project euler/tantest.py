import math
pi = 3.1415926535
halfpi = pi/2
quartpi = halfpi/2


best = 0
for i in range(1,100_000_000):
	if abs(math.tan(i)) > best:
		best=abs(math.tan(i))
		besti=i
		print(besti,math.tan(besti))

