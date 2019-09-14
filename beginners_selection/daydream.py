S = input()
words = ['dream', 'dreamer', 'erase', 'eraser']
while True:
  for word in words:
    if S.endswith(word):
      S = S[:-len(word)]
      if len(S) == 0:
        print('YES')
        exit()
      break
  else:
    print('NO')
    exit()
