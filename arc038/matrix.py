import sys
H, W, A, B = list(map(int, input().split()))

field = [[0 for i in range(W)] for j in range(H)]
h = 0
w = 0
while h + B <= H and w + A <= W:
  for hh in range(h, h + B):
    for ww in range(w, w + A):
      field[hh][ww] = 1
  h += B
  w += A
print(field)
if h == H and w == W:
  for row in field:
    print("".join(map(str, row)))
  sys.exit()
if (H - h == B or H - h == H - B) and (W - w == A or W - w == W - A):
  for hh in range(h, H):
    for ww in range(w, WW):
      field[hh][ww] = 1
  for row in field:
    print("".join(map(str, row)))
  sys.exit()
print("No")
