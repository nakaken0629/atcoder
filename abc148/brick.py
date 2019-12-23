N = int(input())
a = list(map(int, input().split()))

count = 0
i = 0
d = 0
while i + d < len(a):
    if a[i + d] != i + 1:
        d += 1
        count += 1
    else:
        i += 1
if count < N:
    print(count)
else:
    print(-1)