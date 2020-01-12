H, W = list(map(int, input().split()))
S = []
for i in range(H):
    S.append(input())

D = [[None] * W for i in range(H)]
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        if D[h][w] is None:
            d = []
            if h > 0 and not D[h - 1][w] is None:
                d.append(D[h - 1][w] + 1)
            if h < H - 1 and not D[h + 1][w] is None:
                d.append(D[h + 1][w] + 1)
            if w > 0 and not D[h][w - 1] is None:
                d.append(D[h][w - 1] + 1)
            if w < W - 1 and not D[h][w + 1] is None:
                d.append(D[h][w + 1] + 1)
            if d:
                D[h][w] = min(d)
            else:
                D[h][w] = 0
        else:
            None

print(D)