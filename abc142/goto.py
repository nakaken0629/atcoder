N = int(input())
A = list(map(int, input().split()))

AA = dict(zip(A, range(1, len(A) + 1)))
AAA = list(map(lambda x: str(x[1]), sorted(AA.items())))
print(' '.join(AAA))
