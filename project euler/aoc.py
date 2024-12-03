inputs = open("aoctxt.txt")

x = []
c = []

for l in inputs:
	z = l.strip()

	n = z.split(" ")

	x.append(int(n[0]))
	c.append(int(n[3]))

def distance(a,b):
	a.sort()
	b.sort()

	total = 0
	for i in a:
		total += i * b.count(i)
	return total

print(distance(c,x))
distance(c,x)