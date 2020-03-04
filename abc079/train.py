import sys

ABCD = input()
for n in range(2 ** (len(ABCD) - 1)):
    value = ""
    for i in range(len(ABCD) - 1):
        value += ABCD[i]
        if n & (2 ** i) != 0:
            value += "+"
        else:
            value += "-"
    value += ABCD[-1]
    if eval(value) == 7:
        print(value + "=7")
        sys.exit()