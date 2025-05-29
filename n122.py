def complexity(n):
	comp = 0
	while n > 5:

		if n % 2 == 0:
			n //= 2
			comp += 2
		elif n % 3 == 0:
			n //= 3
			comp += 3
		else:
			n -= 1
			comp += 1
	comp += n
	return comp

comps = []
print(complexity(15))

for i in range(1,50):
	comps.append(complexity(i))

print(comps)