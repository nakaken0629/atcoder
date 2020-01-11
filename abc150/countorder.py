import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

all_list = list(itertools.permutations(range(1, N + 1)))
p_index = all_list.index(P)
q_index = all_list.index(Q)
print(abs(p_index - q_index))