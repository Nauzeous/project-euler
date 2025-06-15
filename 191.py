
# maybe one of the easiest ones ive done in a while

def rec(daysleft,os):
	if daysleft == 0:
		return os
	if daysleft > 2:
		return rec(daysleft-1,os+1) + rec(daysleft-2,os+1) + rec(daysleft-3,os+1)
	if daysleft > 1:
		return rec(daysleft-1,os+1) + rec(daysleft-2,os+1)
	return rec(daysleft-1,os+1)

a = rec(31,0)

print(a)