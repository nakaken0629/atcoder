from itertools import groupby
N = int(input())
S = input()
print(len([[k, len(list(g))] for k, g in groupby(S)]))