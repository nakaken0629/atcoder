A, B, C = map(int, input().split())

result = C - (A - B)
if result > 0:
  print(result)
else:
  print(0)

