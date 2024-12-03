

def romparse(letter):
    if letter == "M":
        return 1000
    elif letter == "D":
        return 500
    elif letter == "C":
        return 100
    elif letter == "L":
        return 50
    elif letter == "X":
        return 10
    elif letter == "V":
        return 5
    return 1



def n2r(num) -> str:
    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
    (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    return roman

def r2n(roman_num) -> int:
     d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
     nl = list(roman_num)
     sum = d[nl[len(nl)-1]]
     for i in range(len(nl)-1,0,-1):
             if d[nl[i]]>d[nl[i-1]]:
                     sum -= d[nl[i-1]]
             else:
                     sum += d[nl[i-1]]       
     return sum






file = open("romannums.txt","r")
nums = []
for line in file:
    nums.append(line.strip())

charsaved = 0
for num in nums:
    charsaved += (len(num)-len(n2r(r2n(num))))
print(charsaved)
