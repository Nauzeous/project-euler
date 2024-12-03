from itertools import permutations

# trick for testing divisibility by 11, take alternating sum, so for 21235 2 - 1 + 2 - 3 + 5 = 5, not a multiple of 11 so not a multiple of 11
# start with 10 letter string of numbers from the double pandigital set 00112233445566778899, cant start with 0


pandigits = "12345678901234567890"

possibles = ["".join(p) for p in permutations(pandigits)]

print(possibles)


