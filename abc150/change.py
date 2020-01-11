from math import factorial
N = int(input())
C = list(map(int, input().split()))
C.sort(reverse=True)

ans = 0
for i in range(len(C)):
    ans += (i + 2) * C[i]
print(ans * 2 ** N % (10 ** 9 + 7))