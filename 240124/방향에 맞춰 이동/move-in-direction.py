di = ['W', 'S', 'N', 'E']
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
nx, ny = 0, 0

n = int(input())
dir = []
for i in range(n):
    dir.append(list(input().split()))
    nx += dx[di.index(dir[i][0])] * int(dir[i][1])
    ny += dy[di.index(dir[i][0])] * int(dir[i][1])
print(nx, ny)