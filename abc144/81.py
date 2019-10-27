N = int(input())
answers = set()
for i in range(9):
    for j in range(9):
        answers.add((i + 1) * (j + 1))
if N in answers:
    print("Yes")
else:
    print("No")