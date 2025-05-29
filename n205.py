
# minimum for p is 9, max is 36
# minimum for c is 6, max is 36
# probability generating function for p is (x+1)^4
pcounter = {}
ccounter = {}
newp = [1,1,1,1,1,1,1,1,0]
newc = [1,1,1,1,1,0]
while newp != [4,4,4,4,4,4,4,4,4]:
	newp[8] += 1
	for p in range(8,0,-1):
		if newp[p] == 5:
			newp[p] = 1
			newp[p-1] += 1
		else:
			break
	psum = sum(newp)
	pcounter[psum] = pcounter.get(psum,0) + 1
print(pcounter)
while newc != [6,6,6,6,6,6]:
	newc[5] += 1
	for c in range(5,0,-1):
		if newc[c] == 7:
			newc[c] = 1
			newc[c-1] += 1
		else:
			break
	csum = sum(newc)
	ccounter[csum] = ccounter.get(csum,0) + 1
print(ccounter)

ptotal = 0
ctotal = 0
totalprob = 0
for p in pcounter:
	ptotal += pcounter[p]
for c in ccounter:
	ctotal += ccounter[c]
for p in pcounter:
	pprob = pcounter[p] / ptotal
	for c in ccounter:
		cprob = ccounter[c] / ctotal
		if c < p:
			totalprob += pprob * cprob
		else:
			break

print(totalprob)