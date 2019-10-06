from itertools import product
N = int(input())
S = [input() for i in range(N)]

k = N + 1 # 現在までの最小値
v = [0] * N
p = [range(N) for i in range(N)]
for V_list in product(range(N), range(N), range(N)):
    # すでに最小でない時は次の組み合わせ
    if len(set(V_list)) > k:
        continue

    print(V_list)
