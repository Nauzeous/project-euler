from math import *

# use i for the two similar sides
# use x for remaining side
# i**2 - (x/2)**2 = h
# gen triples with m**2 - s**2, 2*m*s, m**2 + s**2 0 < s < m < k

def gentriples(limit) : 
    totals = 0
    a, m = 0, 2
    triples = []
    while a < limit: 
        for n in range(1, m+1) : 
            h = m**2 - n**2 
            halfx = 2*m*n 
            a = m**2 + n**2 
            if a > limit: 
                break
            if abs(a-halfx*2) == 1: 
                perim = 2*(halfx + a)
                if perim < 1_000_000_000:
                    totals += perim
                    print([halfx*2,a,a], [halfx,h,a], perim)
            elif abs(a-h*2) == 1:
                perim = 2*(h+a)
                if perim < 1_000_000_000:
                    totals += perim
                    print([h*2,a,a],[halfx,h,a],perim)
        m = m + 1
    return totals


triples = gentriples(400_000_000)
print("done", triples)