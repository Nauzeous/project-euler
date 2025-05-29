
def pentagonal_number(k):
    return int(k*(3*k-1) / 2)

def partitions(goal):
    partitions = [1]
    for n in range(1,goal+1):
        partitions.append(0)
        for k in range(1,n+1):
            coeff = [-1,1][k%2==1]
            for t in [pentagonal_number(k), pentagonal_number(-k)]:
                if n >= t:
                    partitions[n] = partitions[n] + coeff*partitions[n-t]
    return partitions


parts = partitions(70_000)
print("done")
for i,p in enumerate(parts):
    #print(p)
    if p % 1_000_000 == 0:
        print(i)
        break