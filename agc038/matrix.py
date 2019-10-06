import sys
H, W, A, B = list(map(int, input().split()))

field = [[0 for i in range(W)] for j in range(H)]
for h in range(B):
  for w in range(A, W):
    field[h][w] = 1
for h in range(B, H):
  for w in range(A):
    field[h][w] = 1
for row in field:
  print("".join(map(str, row)))
