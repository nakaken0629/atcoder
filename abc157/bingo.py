A = []
for _ in range(3):
    A.append(list(map(int, input().split())))
N = int(input())
b = []
for _ in range(N):
    b.append(int(input()))

for num in b:
    for x in range(3):
        for y in range(3):
            if A[x][y] == num:
                A[x][y] = -1

amount = 0
for x in range(3):
    if max(A[x]) == -1:
        amount += 1
for y in range(3):
    if max([A[0][y], A[1][y], A[2][y]]) == -1:
        amount += 1
if max([A[0][0], A[1][1], A[2][2]]) == -1:
    amount += 1
if max([A[2][0], A[1][1], A[0][2]]) == -1:
    amount += 1

if amount > 0:
    print("Yes")
else:
    print("No")