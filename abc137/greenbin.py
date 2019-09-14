N = int(input())
s_dict = {}
for i in range(N):
  s = "".join(sorted(input()))
  if s in s_dict:
    s_dict[s] += 1
  else:
    s_dict[s] = 1
result = sum(v * (v - 1) // 2 for v in s_dict.values())
print(result)

