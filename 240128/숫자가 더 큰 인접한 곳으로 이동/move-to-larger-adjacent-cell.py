n, x, y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
move_num = []
x, y = x - 1, y - 1
move_num.append(arr[x][y])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

move_cnt = 1

def move(x, y):
    max_num = arr[x][y]
    for dir_num in range(4):
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if in_range(nx, ny) and arr[nx][ny] > max_num:
            x, y = nx, ny
            max_num = arr[nx][ny]
            move_num.append(arr[nx][ny])
            
move(x, y)

for i in range(len(move_num)):
    print(move_num[i], end=" ")