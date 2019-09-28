import fractions

A, B = list(map(int, input().split()))

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

l = sorted(list(set(make_divisors(A)) & set(make_divisors(B))))
#print(l)
i = 0
while i < len(l):
    v = l[i]
    if v == 1:
        i += 1
        continue
    l = l[0:i+1] + list(filter(lambda x: x % v != 0, l[i+1:]))
#    print(l)
    i += 1
print(len(l))

