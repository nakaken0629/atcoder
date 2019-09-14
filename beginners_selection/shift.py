import sys
n = input()
l = [int(s) for s in input().split()]
count = 0

while True:
  for i in range(len(l)):
    v = l[i]
    if v % 2 != 0:
      print(count)
      sys.exit()
    else:
      l[i] = v / 2
  count += 1
