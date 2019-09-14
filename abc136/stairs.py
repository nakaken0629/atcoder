N = input()
H_list = list(map(int, input().split()))

for i in range(len(H_list) - 1):
  if H_list[i] < H_list[i + 1]:
    H_list[i + 1] -= 1
  if H_list[i] > H_list[i + 1]:
    print('No')
    exit()
print('Yes')
