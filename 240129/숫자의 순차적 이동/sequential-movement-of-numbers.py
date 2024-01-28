n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_pos(num):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == num:
                return(i, j)
            
def next_pos(x, y):
    max_num = 0
    max_pos = (-1, -1)
    for dir_num in range(8):
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if in_range(nx, ny) and arr[nx][ny] > max_num:
            max_num = arr[nx][ny]
            max_pos = (nx, ny)
    x, y = max_pos
    return x, y

def switch(x, y):
    global arr
    nx, ny = next_pos(x, y)
    tmp = arr[nx][ny]
    arr[nx][ny] = arr[x][y]
    arr[x][y] = tmp


for i in range(m):
	for num in range(1, n * n + 1):
		x, y = find_pos(num)
		switch(x, y)
    

for r in range(n):
    for c in range(n):
        print(arr[r][c], end=" ")
    print()