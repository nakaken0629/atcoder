S = input()

amount = 0
for n in range(2 ** (len(S) - 1)):
    s = ""
    nn = n
    for i in range(len(S) - 1):
        s += S[i]
        if nn % 2 == 1:
            s += "+"
        nn >>= 1
    s += S[-1]
    amount += eval(s)
print(amount)