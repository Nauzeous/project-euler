import math

file = open("words.txt")

def isanagram(w1,w2):
	return(sorted(w1)==sorted(w2))

def formatanagram(w1,w2,numlets):
	word1 = [l for l in w1]
	word2 = [l for l in w2]
	form = "abcdefghijk"
	formatted = ["s" for i in range(numlets+1)]
	for i,n in enumerate(word1):
		formatted[word2.index(n)]=form[i]
		word2[word2.index(n)]="s"
	fin = "".join(formatted) 
	return fin[:-1]


def findanagrams(wordlist):
	anagrams = []
	length = len(wordlist)
	for i in range(length):

		for j in range(i+1,length):
			if isanagram(wordlist[i],wordlist[j]):
				anagrams += [[wordlist[i],wordlist[j]]]
	return anagrams

words = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for line in file:
	l = line.strip()
	wordlis = l.split("\",\"")
for w in wordlis:
	words[len(w)-1].append(w)

squares = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for i in range(1,100000):
	isq = str(i**2)
	squares[len(isq)].append(isq)



numletters = 9
#sqanagrams = findanagrams(squares[numletters])
wordanagrams = findanagrams(words[numletters-1])
formatagrams = [formatanagram(p[0],p[1],numletters) for p in wordanagrams]

#for pair in sqanagrams:
#	pair1 = formatanagram(pair[0],pair[1],numletters)
#	pair2 = formatanagram(pair[1],pair[0],numletters)
#	print(pair[0],pair[1])
#	print(pair1,pair2)
#	if pair1 in formatagrams or pair2 in formatagrams:
#		print(pair, pair1, pair2)

print(math.sqrt(8732025))
print(math.sqrt(18769))