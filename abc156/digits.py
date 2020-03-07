N, K = list(map(int, input().split()))

digit = 1
while N >= K:
    N //= K
    digit += 1
print(digit)