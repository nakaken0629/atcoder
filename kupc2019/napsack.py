n, m, W = list(map(int, input().split()))
wv = []
for i in range(n):
    w, v = list(map(int, input().split()))
    wv.append([w, v])
ab = []
for i in range(m):
    a, b = list(map(int, input().split()))
    ab.append([a, b])

# グラフごとにグルーピング
group = [None] * n
next_index = 0
for a, b in ab:
    a -= 1
    b -= 1
    if group[a] == None and group[b] == None:
        group[a] = next_index
        group[b] = next_index
        next_index += 1
    elif group[a] == None:
        group[a] = group[b]
    elif group[b] == None:
        group[b] = group[a]
    else:
        min_value = min(group[a], group[b])
        max_value = max(group[a], group[b])
        for i in range(n):
            if group[i] == max_value:
                group[i] == min_value
for i in range(n):
    if group[i] == None:
        group[i] = next_index
        next_index += 1

group_set = set(group)
print(group_set)