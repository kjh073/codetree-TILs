n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dir_c = {}

dir_c['D'] = 0
dir_c['R'] = 1
dir_c['L'] = 2
dir_c['U'] = 3

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
x, y = r - 1, c - 1
nx, ny = r - 1, c - 1
dir_num = dir_c[d]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for i in range(t):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if not in_range(nx, ny):
        dir_num = 3 - dir_num
        continue
    x, y = nx, ny

print(x + 1, y + 1)