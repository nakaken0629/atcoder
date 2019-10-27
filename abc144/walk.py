import math
N = int(input())
n = int(math.sqrt(N)) + 1
for i in reversed(range(n)):
    if N % i == 0:
        a = i
        b = N // i
        print(a + b - 2)
        break