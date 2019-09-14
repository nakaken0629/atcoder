S = input()
S_len = len(S)
for i in range(S_len):
  print(i, end=":")
  result = 0
  # 右方向
  check = "RL"
  j = i
  while j < S_len - 1:
    if S[j:j+2] != check:
      break
    print(S[j:j+2], end=" ")
    result += 1
    if check == "RL":
      check = "LL"
      j += 1
    else:
      j += 2
  print("*", end=" ")
  # 左方向
  check = "RL"
  j = i
  while j > 0:
    if S[j-1:j+1] != check:
      break
    print(S[j-1:j+1], end=" ")
    result += 1
    if check == "RL":
      check = "RR"
      j -= 1
    else:
      j -= 2
  print(result)
print()
