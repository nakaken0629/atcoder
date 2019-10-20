N, X = list(map(int, input().split()))
a = list(map(int, input().split()))
a_max = max(a)
result = 0
for i in range(N):
    if a[i] + X >= a_max:
        result += 1
print(result)
