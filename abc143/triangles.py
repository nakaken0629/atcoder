import itertools
N = int(input())
L = tuple(map(int, input().split()))
tri = set()
for i in itertools.combinations(L, 3):
    tri.add(tuple(sorted(i)))
sum = 0
for t in tri:
    if(t[0] + t[1] > t[2]):
        sum += 1
print(sum)