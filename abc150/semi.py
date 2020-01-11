from fractions import gcd
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

def lcm(values):
    ans = values[0]
    for i in range(1, len(values)):
        ans = ans * values[i] // gcd(ans, values[i])
    return ans

min_value = lcm(A)
amount = M * 2 // min_value
print((amount + 1) // 2)
