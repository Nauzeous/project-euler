def hypex(n,k):
	tower = [1777 for i in range(1856)]


t = 1777

for i in range(1855):
	t = pow(t,t,10_000_000)

print(t)

