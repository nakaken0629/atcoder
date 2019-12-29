X = int(input())

import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

x = X
while(not is_prime(x)):
    x += 1
print(x)