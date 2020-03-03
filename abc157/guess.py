import sys

N, M = list(map(int, input().split()))
sc_list = []
for _ in range(M):
    sc_list.append(list(map(int, input().split())))

if N == 1:
    nums = range(10)
elif N == 2:
    nums = range(10, 100)
else:
    nums = range(100, 1000)

for num in nums:
    for s, c in sc_list:
        if s > N:
            break
        if int(str(num)[s - 1]) != c:
            break
    else:
        print(num)
        sys.exit(0)
print(-1)