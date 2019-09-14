a, b = map(int, input().split())
is_even = (a % 2 == 0 or b % 2 == 0)
if is_even:
  print("Even")
else:
  print("Odd")
