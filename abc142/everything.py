import itertools

N, M = list(map(int, input().split()))
a = []
b = []
c = []
for m in range(M):
    am, bm = list(map(int, input().split()))
    a.append(am)
    b.append(bm)
    cm = list(map(int, input().split()))
    c.append(cm)

x = range(N)

for L in range(0, len(x)+1):
        for subset in itertools.permutations(x, L):
                print(subset)
