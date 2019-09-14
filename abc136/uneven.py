N = int(input())

result = 0
if N < 10:
  result = N
elif N < 100:
  result = 9
elif N < 1000:
  result = 9 + (N - 100 + 1)
elif N < 10000:
  result = 9 + 900
elif N < 100000:
  result = 9 + 900 + (N - 10000 + 1)
else:
  result = 9 + 900 + 90000
print(result)
