N, A, B = map(int, input().split())
result = 0
for n in range(1, N + 1):
  nn = n // 10000 + n % 10000 // 1000 + n % 1000 // 100 + n % 100 // 10 + n % 10
  if A <= nn and nn <= B:
    result += n
print(result)
