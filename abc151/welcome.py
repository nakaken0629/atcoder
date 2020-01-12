N, M = list(map(int, input().split()))
questions = []
for i in range(M):
    p, S = list(input().split())
    questions.append([int(p), S])

ac_list = [0] * N
wa_list = [0] * N

for p, S in questions:
    if S == 'AC':
        ac_list[p - 1] = 1
    else:
        if ac_list[p - 1] == 1:
            continue
        wa_list[p - 1] += 1

for i in range(N):
    if ac_list[i] == 0:
        wa_list[i] = 0

print(sum(ac_list), sum(wa_list))
