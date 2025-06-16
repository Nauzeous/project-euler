def prob(req_blue,turn):
	if req_blue <= 0:
		return 1
	if turn == 16:
		return 0

	p = 0
	pb = 1/(turn+1)
	p += pb * prob(req_blue-1,turn+1)
	p += (1-pb) * prob(req_blue,turn+1)
	return p

ans = prob(8,1)

print(int(1/ans))
