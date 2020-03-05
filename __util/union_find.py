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
