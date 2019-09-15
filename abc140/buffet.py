N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

score = 0
last_i = -2
for index in range(N):
  i = A[index]
  score += B[i - 1]
  if i == last_i + 1:
    score += C[last_i - 1]
  last_i = i
print(score)
