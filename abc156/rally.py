from statistics import mean

N = int(input())
A_list = list(map(int, input().split()))

ave = mean(A_list)
ave_r = round(ave)

dist = 0
for A in A_list:
    dist += (A - ave_r) ** 2
print(dist)