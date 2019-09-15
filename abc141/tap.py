S = input()

S_odd = S[::2]
S_even = S[1::2]
if 'L' in S_odd or 'R' in S_even:
  print("No")
else:
  print("Yes")
