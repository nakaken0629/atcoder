from itertools import permutations

N = int(input())
X = list(map(int, input().split()))

cases = permutations(range(N - 1))
print(len(list(cases)))
# size = len(cases)
# score = 0
# for case in cases:
#     flags = [1] * N
#     for i in case:
#         flags[i] = 0
#         j = i + 1
#         while(flags[j] == 0):
#             j += 1
#         score += X[j] - X[i]
# print(score // size)