N, A, B = list(map(int, input().split()))

d = N // (A + B)
m = N % (A + B)

print(d, m)

answer = d * A
if m <= A:
    answer += m
else:
    answer += A

print(answer)