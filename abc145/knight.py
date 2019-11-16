import sys, math

mod = 1000000007

def mod_combination(n, k, mod = 10 ** 9 + 7):
    def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)
        d, x, y = extended_gcd(b, a % b)
        return (d, y, x - (a // b) * y)
    p, q = 1, 1
    for i in range(n - k + 1, n + 1):
        p = (p * i) % mod
    for i in range(2, k + 1):
        q = (q * i) % mod
    return p * (extended_gcd(q, mod)[1] % mod) % mod

X, Y = list(map(int, input().split()))

if X > Y * 2 or Y > X * 2:
    print(0)
    sys.exit()
if (X + Y) % 3 != 0:
    print(0)
    sys.exit()

distance = (X + Y) // 3
x = (X - distance)
y = (Y - distance)
print(mod_combination(distance, x))