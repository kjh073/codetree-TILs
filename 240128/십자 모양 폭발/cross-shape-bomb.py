n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r - 1, c - 1

size = arr[r][c]
tmp_arr = [[0] * n for _ in range(n)]

def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def bomb_range_c():
    for i in range(1, size):
        if in_range(r - i, c):
            arr[r - i][c] = 0
        if in_range(r + i, c):
            arr[r + i][c] = 0

def bomb_range_r():
    for i in range(1, size):
        if in_range(r, c - i):
            arr[r][c - i] = 0
        if in_range(r, c + i):
            arr[r][c + i] = 0

def gravity_num(c):
    tmp_i = n - 1
    for i in range(n - 1, -1, -1):
        if arr[i][c] != 0:
            tmp_arr[tmp_i][c] = arr[i][c]
            tmp_i -= 1
            
bomb_range_c()
bomb_range_r()
arr[r][c] = 0

for c in range(n):
    gravity_num(c)

for i in range(n):
    for j in range(n):
        print(tmp_arr[i][j], end=" ")
    print()