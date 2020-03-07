N, P = list(map(int, input().split()))
S = input()

N = 2 * 10 ** 5
S = "1" * N
print(S)
print(N)

amount = 0
len_S = len(S)
for i in range(len_S+ 1):
    for j in range(i + 1, len_S + 1):
        pass
        # n = int(S[i:j])
        # if n % P == 0:
        #     amount += 1
print(amount)

# P_multi = []
# for i in range(P, 10 ** N, P):
#     P_multi.append(str(i))