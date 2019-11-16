import math
import itertools
N = int(input())
xy_list = []
for i in range(N):
    xy_list.append(list(map(int, input().split())))
distance = 0
count = 0
permutations = itertools.permutations(xy_list)
for permutation in permutations:
    count += 1
    for i in range(len(permutation) - 1):
        xi = permutation[i][0]
        yi = permutation[i][1]
        xj = permutation[i + 1][0]
        yj = permutation[i + 1][1]
        d = math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
        distance += d
print(distance / count)
