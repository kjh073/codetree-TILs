from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
def in_range(x, y):
    return 0 <= x < n and  0 <= y < m 

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and arr[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))

visited[0][0] = True
q.append((0, 0))
bfs()

if visited[n - 1][m - 1] == True:
    print(1)
else:
    print(0)