import math
import bisect

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()

for i in range(M):
  if (N > 1 and A[-1] < A[-2]):
    a = A.pop(-1)
    bisect.insort(A, a)
  A[-1] /= 2.0

amount = 0
for a in A:
  amount += math.floor(a)
print(amount)
