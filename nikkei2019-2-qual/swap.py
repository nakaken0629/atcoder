import sys
from math import ceil
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_AB = sorted(zip(B, A))
sorted_A, sorted_B = zip(*sorted_AB)
print(sorted_A, sorted_B)

swaps = 0
for i in range(N):
    if sorted_A[i] <= sorted_B[i]:
        continue
     