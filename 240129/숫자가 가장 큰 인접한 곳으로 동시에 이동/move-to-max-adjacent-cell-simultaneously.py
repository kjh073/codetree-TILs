n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = [[0] * n for _ in range(n)]
next_cnt = [[0] * n for _ in range(n)]
marble_cnt = 0

for _ in range(m):
    r, c = map(int, input().split())
    cnt[r - 1][c - 1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def next_pos(x, y):
    max_num = arr[x][y]
    max_pos = (-1, -1)
    for dir_num in range(4):
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if in_range(nx, ny) and arr[nx][ny] > max_num:
            max_num = arr[nx][ny]
            max_pos = (nx, ny)
    x, y = max_pos
    return x, y

def move(x, y):
    nx, ny = next_pos(x, y)
    next_cnt[nx][ny] += 1

def is_marble():
    for i in range(n):
        for j in range(n):
            if cnt[i][j] == 1:
                move(i, j)

def copy(cnt, next_cnt):
    for i in range(n):
        for j in range(n):
            if next_cnt[i][j] > 1:
                continue
            else:
                cnt[i][j] = next_cnt[i][j]
    
for _ in range(t):
    is_marble()
    copy(cnt, next_cnt)

for i in range(n):
    for j in range(n):
        if cnt[i][j] == 1:
            marble_cnt += 1
print(marble_cnt)