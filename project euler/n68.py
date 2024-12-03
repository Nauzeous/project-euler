from itertools import permutations

nums = [1,2,3,4,5,7,8,9,10]

def validngon(ngon):
	for i in range(4):
		total = 14
		if ngon[0+i*2] + ngon[1+i*2] + ngon[3+i*2] != total:
			return False
	if ngon[8]+ngon[9]+ngon[1] != total:
		return False
	if ngon.index(10) % 2 == 0:
		return True


combs = [[6]+list(p) for p in permutations(nums)]

comf = [comb for comb in combs if validngon(comb)]

print(comf)

def convngon(ngon):
	formatted = [ngon[0],ngon[1],ngon[3],ngon[2],ngon[3],ngon[5],ngon[4],ngon[5],ngon[7],ngon[6],ngon[7],ngon[9],ngon[8],ngon[9],ngon[1]]
	return formatted

print(convngon([6, 5, 10, 3, 9, 1, 8, 4, 7, 2]))