from operator import add
from functools import reduce

N, K = list(map(int, input().split()))
R, S, P = list(map(int, input().split()))
T = list(input())
for i in range(N - K):
    s1 = T[i]
    s2 = T[i + K]
    if s1 == s2:
        T[i + K] = "0"
score = T.count("r") * P + T.count("s") * R + T.count("p") * S
print(score)
