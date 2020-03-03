import collections

def DFS(graph, start, end, mark_dict):
    mark_dict[start] = True
    for target in graph[start]:
        if target == end:
            break
        elif target not in mark_dict:
            mark_dict[target] = True
            DFS(graph, target, end, mark_dict)
            
N, M, K = list(map(int, input().split()))
AB_list = []
for _ in range(M):
    AB_list.append(sorted(list(map(int, input().split()))))
AB_list.sort()
CD_list = []
for _ in range(K):
    CD_list.append(sorted(list(map(int, input().split()))))
CD_list.sort()

graph = [[] for _ in range(N)]
for A, B in AB_list:
    graph[A - 1].append(B - 1)
    graph[B - 1].append(A - 1)

answer = [0] * N
print(answer)
for n1 in range(N):
    for n2 in range(N):
        if [n1, n2] in AB_list:
            continue
        if [n1, n2] in CD_list:
            continue
        mark_dict = {}
        for n in range(N):
            mark_dict[n] = False
        DFS(graph, n1, n2, mark_dict)
    