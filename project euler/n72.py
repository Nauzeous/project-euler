from math import gcd

def generate_moebius_function(ceiling: int) -> list[int]:
    moebius = [None] * ceiling
    moebius[1] = 1
    for i in range(2, ceiling):
        # If we found a prime, set it to -1.
        if moebius[i] is None:
            moebius[i] = -1
            # Tick off the multiples.
            for k in range(2 * i, ceiling, i):
                if moebius[k] is None:
                    moebius[k] = -1
                else:
                    moebius[k] *= -1
            # Eliminate all squares.
            for k in range(i**2, ceiling, i**2):
                moebius[k] = 0
    return moebius

def summary_totient(ceiling: int) -> int:
    moebius = generate_moebius_function(ceiling + 1)
    result = 0
    for k in range(1, ceiling + 1):
        floor = ceiling // k
        result += moebius[k] * (floor) * (1 + floor)
    return result // 2


print(summary_totient(1_000_000))