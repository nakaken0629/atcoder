import sys
from itertools import groupby
S = input()
K = int(input())

# 文字列分割
s = [[k, len(list(g))] for k, g in groupby(S)]

# 単一文字の場合は特別処理
if len(s) == 1:
#    print("単一文字")
    print(len(S) * K // 2)
    sys.exit()

# 単位文字列で置換する
s_count = sum(ss[1] // 2 for ss in s)
result = s_count * K

# 最初と最後の文字が同じで、かつ最初か最後の文字列が奇数だった場合の調整
# print(s[0], s[-1])
if s[0][0] == s[-1][0] and (s[0][1] % 2 == 1 and s[-1][1] % 2 == 1):
#    print("調整あり")
    result += K - 1

print(result)
