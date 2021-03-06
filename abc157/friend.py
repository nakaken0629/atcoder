class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parents = [i for i in range(N)]
        self.sizes = [1] * N

    def root(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.root(self.parents[x])
        return self.parents[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx < ry:
            self.parents[ry] = rx
            self.sizes[rx] += self.sizes[ry]
            self.sizes[ry] = 0
        elif rx > ry:
            self.parents[rx] = ry
            self.sizes[ry] += self.sizes[rx]
            self.sizes[rx] = 0

    def same(self, x, y):
        return self.root(x) == self.root(y)
    
    def size(self, x):
        return self.sizes[self.root(x)]

N, M, K = list(map(int, input().split()))
AB_list = []
for _ in range(M):
    A, B = list(map(int, input().split()))
    AB_list.append([A - 1, B - 1])
CD_list = []
for _ in range(K):
    C, D = list(map(int, input().split()))
    CD_list.append([C - 1, D - 1])

uf = UnionFind(N)
for A, B in AB_list:
    uf.unite(A, B)

friends = [0] * N
for A, B in AB_list:
    friends[A] += 1
    friends[B] += 1
blocks = [0] * N
for C, D in CD_list:
    if uf.root(C) != uf.root(D):
        continue
    blocks[C] += 1
    blocks[D] += 1
answers = [0] * N
for i in range(N):
    answers[i] = uf.size(i) - 1 - friends[i] - blocks[i]

print(" ".join(map(str, answers)))