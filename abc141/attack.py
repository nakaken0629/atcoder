N, K, Q = list(map(int,input().split()))
A = [int(input()) for i in range(Q)]
score = [0] * N
for i in range(Q):
  score[A[i] - 1] += 1
for i in range(N):
  result = K - Q + score[i]
  if result > 0:
    print("Yes")
  else:
    print("No")
