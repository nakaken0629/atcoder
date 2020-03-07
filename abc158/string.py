S = input()
Q = int(input())
queries = []
for _ in range(Q):
    queries.append(input())

left = ""
right = ""
target = 0

for query in queries:
    if query == "1":
        target = 1 - target
    else:
        _, F, C = list(query.split())
        if F == "1":
            if target == 0:
                left += C
            else:
                right += C
        else:
            if target == 0:
                right += C
            else:
                left += C
if target == 0:
    print("{}{}{}".format(left[::-1], S, right))
else:
    print("{}{}{}".format(right[::-1], S[::-1], left))
