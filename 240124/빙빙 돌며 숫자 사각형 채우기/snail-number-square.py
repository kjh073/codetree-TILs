n, m = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
dir_num = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

arr = [[0 for _ in range(m)] for _ in range(n)]

for i in range(1, n * m + 1):
    arr[x][y] = i
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if in_range(nx, ny) and arr[nx][ny] == 0:
        x, y = nx, ny
    else:
        dir_num = (dir_num + 1) % 4
        x += dx[dir_num]
        y += dy[dir_num]

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()