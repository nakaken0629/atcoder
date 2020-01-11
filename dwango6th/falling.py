N = int(input())
playlist = []
for i in range(N):
    s, t = list(input().split())
    playlist.append([s, int(t)])
X = input()

time = 0
is_sleep = False
for s, t in playlist:
    if is_sleep:
        time += t
    if s == X:
        is_sleep = True

print(time)