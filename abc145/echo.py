import sys
N = int(input())
S = input()
if N % 2 == 1:
    print("No")
    sys.exit()
n = N // 2
if S[:n] != S[n:]:
    print("No")
else:
    print("Yes")