global squares



def checkworks(c1,c2): # 01 04 09 16 25 36 49 64 81
	valid = True
	if cmd(c1,c2,'01') == 0:valid=False
	if cmd(c1,c2,'04') == 0:valid=False
	if cmd(c1,c2,'09') == cmd(c1,c2,'06') == 0:valid=False
	if cmd(c1,c2,'16') == cmd(c1,c2,'19') == 0:valid=False
	if cmd(c1,c2,'25') == 0:valid=False
	if cmd(c1,c2,'36') == cmd(c1,c2,'39') == 0:valid=False
	if cmd(c1,c2,'49') == cmd(c1,c2,'46') == 0:valid=False
	if cmd(c1,c2,'64') == cmd(c1,c2,'94') == 0:valid == False
	if cmd(c1,c2,'81') == 0:valid=False
	return valid


def cmd(cube1,cube2,sq):
	tcube1 = cube1[:]
	tcube2 = cube2[:]
	valid = False
	if sq[0] in cube1:
		if sq[1] in cube2:
			valid = True
	if sq[0] in cube2:
		if sq[1] in cube1:
			valid = True

	return valid



print(checkworks(['0','5','6','7','8','6'],['1','2','3','4','8','9']))

nums = ['0','1','2','3','4','5','6','7','8','9']

cubes = []

for a in nums:
	nums1=nums[:]
	nums1.remove(a)
	for b in nums1:
		nums2=nums1[:]
		nums2.remove(b)
		for c in nums2:
			nums3 = nums2[:]
			nums3.remove(c)
			for d in nums3:
				nums4 = nums3[:]
				nums4.remove(d)
				for e in nums4:
					nums5 = nums4[:]
					nums5.remove(e)
					for f in nums5:
						cubes.append( sorted([a,b,c,d,e,f]) )

rcubes = []

for c in cubes:
	if c in rcubes:
		continue
	rcubes.append(c) 
total = 0
for i in range(len(rcubes)):
	for j in rcubes[i:]:
		total += checkworks(rcubes[i],j)

print(total)


