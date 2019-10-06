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

digits = len(format(2 ** N - 1, 'b'))
for i in range(2 ** N):
    use = format(i, 'b').zfill(digits)
    boxes = set(aa if use[for j in a)
    print(boxes)