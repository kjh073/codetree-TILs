n, x, y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
move_num = []
x, y = x - 1, y - 1
move_num.append(arr[x][y])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(x, y):
    max_num = arr[x][y]
    max_x, max_y = x, y
    while True:
        for dir_num in range(4):
            nx = x + dx[dir_num]
            ny = y + dy[dir_num]
            pre_max_x, pre_max_y = x, y
            if in_range(nx, ny) and arr[nx][ny] > max_num:
                x, y = nx, ny
                max_x, max_y = x, y
                max_num = arr[x][y]
                move_num.append(arr[x][y])
                break
        # print(max_x, max_y, pre_max_x, pre_max_y)
        if max_x == pre_max_x and pre_max_y == y:
            break
            
move(x, y)

for i in range(len(move_num)):
    print(move_num[i], end=" ")