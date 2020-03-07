from math import floor, ceil

A, B = list(map(int, input().split()))

pa1 = ceil(A * 100 / 8.0)
pa2 = floor((A * 100 + 100) / 8.0)
pb1 = ceil(B * 100 / 10.0)
pb2 = floor((B * 100 + 100) / 10.0)

p1 = max(pa1, pb1)
if p1 >= pa2 or p1 >= pb2:
    print(-1)
else:
    print(p1)
