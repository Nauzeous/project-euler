from collections import defaultdict
import sys

# this is terrible, uses 10gb RAM and took 4 minutes to complete
# the fact i have to change the recursion limit is proof of this
sys.setrecursionlimit(20000)


memo = [[0 for i in range(12346)] for j in range(24692>>1)]
def prob(r,b):
	global memo

	if r == 0:
		return 1

	if b == 0:
		return 0

	if memo[r>>1][b] != 0:
		return memo[r>>1][b]


	p = 0
	cards = b + r
	prb = r/cards * b/(cards-1) + b/cards * r/(cards-1) # 1 red 1 black
	prr = r/cards * (r-1)/(cards-1) # 2 red




	if prb != 0:
		p+=prob(r,b-1)*prb

	if prr != 0:
		p+=prob(r-2,b)*prr

	pnbb = prb+prr # chance you dont get 2 black

	# geometric sequence, p + pbb*p + pbb^2*p
	# pnbb is 1 - pnb
	ret = p/pnbb
	memo[r>>1][b] = ret
	return ret


answer = prob(24690,12345)

print(answer)