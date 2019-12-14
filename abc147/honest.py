N = int(input())
A = []
xy = []
for i in range(N):
    A_ = int(input())
    A.append(A_)
    xy_ = []
    xy.append(xy_)
    for j in range(A_):
        xy_.append(list(map(int, input().split())))
answer = 0
for i in range(2 ** N):
    peoples = format(i, "0{0}b".format(N))
    num = peoples.count('1')
    if num <= answer:
        continue
    for j in range(len(peoples)):
        people = peoples[j]
        if people == '0':
            continue
        for x, y in xy[j]:
            if peoples[x - 1] != str(y):
                break
        else:
            continue
        break
    else:
        answer = num
print(answer)
