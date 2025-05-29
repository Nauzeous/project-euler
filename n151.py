def split(card):
	if card == 5:
		return []
	elif card == 4:
		return [5]
	elif card == 3:
		return [4,5]
	return [3,4,5]

global fives
fives = 0

def foo(arr,ret,memo):
	global fives
	arr = sorted(arr)

	if arr == [5]:
		return 0
	if arr in memo[0]:
		return memo[1][memo[0].index(arr)]

	if len(arr) == 1:
		ret += 1


	for i in range(len(arr)):
		fives += 1
		ret += foo(arr[:i] + split(arr[i]) + arr[i+1:],ret,memo)


	if arr == [2,3,4,5]:
		print(memo)
		return ret

	if arr not in memo:
		memo[0].append(arr)
		memo[1].append(ret)


	return ret


env = [2,3,4,5]

val = foo(env,0,[[],[]])

print(val)





