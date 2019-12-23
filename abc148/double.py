import sys
N = int(input())
if N % 2 != 0:
    print(0)
    sys.exit()

answer = 0
for i in range(36, 0, -1):
    n = 5 ** i
    answer += (N // n // 2)
print(answer)