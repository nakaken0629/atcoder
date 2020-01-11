from fractions import gcd
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

def lcm(values):
    ans = values[0]
    for i in range(1, len(values)):
        ans = ans * values[i] // gcd(ans, values[i])
    return ans

def count_div2(value):
    count = 0
    while value % 2 == 0:
        count += 1
        value //= 2
    return count

min_value = lcm(A)
amount = M * 2 // min_value

div2 = count_div2(A[0])
if any([count_div2(a) != div2 for a in A]):
    print(0)
else:
    print((amount + 1) // 2)
