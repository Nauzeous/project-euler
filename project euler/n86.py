import time, math

def combinations(a, bc):
    if 2*a < bc:
        return 0
    elif a >= bc:
        return (bc//2)
    else:
        if bc % 2 == 0:
            return a + 1 - ((bc)//2)
        else:
            return a - ((bc-1)//2)
    
def ppt(N): #Pythagorean Triplet generator
    limit = 10**4
    triples = [0]*(limit + 1)
    for m in range(1,int(math.sqrt(2*limit))+1):
        for n in range(1,m):
            if (m+n) % 2 == 1 and math.gcd(m,n) == 1:
                #a = m**2 + n**2 #not needed for this problem
                b = m**2 - n**2
                c = 2*m*n
                #Case 1
                for k in range(1, int(limit/b) + 1):
                    triples[k*b] += combinations(k*b, k*c)
                
                #Case 2 
                for k in range(1, int(limit/c) + 1):
                    triples[k*c] += combinations(k*c, k*b)
    
    #return sum(triples[:101])

    total = 0
    for x in range(len(triples)):
        total += triples[x]
        if total > N:
            return x

if __name__ == "__main__":
    k = input("Input an integer: ")
    temp = ppt(int(k))
    print(temp)
