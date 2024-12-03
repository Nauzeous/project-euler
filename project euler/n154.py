layer = 200_000
def factorial25(n):
	twos = 0
	fives = 0

	tk = 2

	while tk <= n:
		twos += n // tk
		tk *= 2

	fk = 5

	while fk <= n:
		fives += n // fk
		fk *= 5

	return twos,fives

terms = 0.5 * (layer+1) * (layer+2)

def checkabc(a,b,c):
	at,af = factorial25(a)
	bt,bf = factorial25(b)
	ct,cf = factorial25(c)
	if at + bt + ct <= 199982:
		return False
	if af + bf + cf <= 49986:
		return False
	return True

twoslim = 199982
fiveslim = 49986
for i in range(layer+1):
	print(i)
	layerterms = 0
	off = (i) % 2
	end = layer - i + off
	linelength = (layer + 1  - i)
	for j in range(linelength//2):
		c = j
		a = layer - j - i
		b = i
		layerterms += checkabc(a,b,c)
	terms -= layerterms * 2
	if i % 2 == 0:
		terms -= checkabc(linelength // 2,i,linelength // 2)


print(terms)