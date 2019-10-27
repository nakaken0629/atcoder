N, K = list(map(int, input().split()))
A = sorted(list(map(int, input().split())))
lenA = len(A)
F = sorted(list(map(int, input().split())))

index = 0
for i in range(len(A)):
    ii = lenA - i - 1
    if A[ii] < K:
        K -= A[ii]
        A[ii] = 0
        index += 1
    else:
        A[ii] -= K
        K = 0
        break
print(A)
print(F)
sum = 0
for i in range(len(A) - index):
    sum = max(sum, A[i] * F[i])

print(sum)
