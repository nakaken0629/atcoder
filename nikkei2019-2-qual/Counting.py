import sys
import collections

N = int(input())
D = list(map(int,input().split()))

if D[0] != 0:
    print(0)
    sys.exit()
DD = collections.Counter(D)
max_key = max(DD.keys())
result = 1
last_v = 0
for k in range(max_key + 1):
    if not k in DD:
        print(0)
        sys.exit()
    v = DD[k]
    if k == 0:
        if v > 1:
            print(0)
            sys.exit()
        last_v = v
        continue
    result *= last_v ** v
    last_v = v
print(result % 998244353)
