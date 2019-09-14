N = int(input())
ti, xi, yi = 0, 0, 0
for i in range(N):
  tj, xj, yj = map(int, input().split())
  d = abs(xi - xj) + abs(yi - yj)
  t = tj - ti
  if d > t or (t - d) % 2 == 1:
    print('No')
    exit()
  ti, xi, yi = tj, xj, yj
print('Yes')
