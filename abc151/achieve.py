N, K, M = list(map(int, input().split()))
A = list(map(int, input().split()))

border = N * M
score = sum(A)
d = border - score
if d < 0:
    print(0)
elif d <= K:
    print(d)
else:
    print(-1)