from bisect import bisect_left,bisect

N, K = list(map(int, input().split()))
h = list(map(int, input().split()))

h.sort()
index = bisect_left(h, K)
print(N - index)
