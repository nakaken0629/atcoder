from operator import itemgetter, attrgetter
N, M = map(int, input().split())
AB_list = []
for i in range(N):
  A, B = map(int, input().split())
  if A <= M:
    AB_list.append([A, B])
  AB_list.sort(key=itemgetter(1, 0), reverse=True)
result = 0
i = 0
for m in range(M, 0, -1):
  while i < len(AB_list):
    a, b = AB_list[i]
    if a <= m:
      result += b
      AB_list.pop(i)
      break
    i += 1
print(result)
