import math
a, b, x = list(map(int, input().split()))
xx = x / a
if xx <= a * b / 2:
    print("low")
    print(90 - math.atan(2 * xx / b ** 2) * 180 / math.pi)
else:
    print("high")
    print(-math.atan(2 * (xx - a * b) / a ** 2) * 180 / math.pi)