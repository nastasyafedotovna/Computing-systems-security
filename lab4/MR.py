import numpy as np
import math


def miller_rabin(n):
    d, s = n - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2

    rounds = int(math.log2(n))
    for i in range(rounds):
        a = np.random.randint(2, rounds + 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
            if x == 1:
                return 0
        else:
            return 0
    return 1
