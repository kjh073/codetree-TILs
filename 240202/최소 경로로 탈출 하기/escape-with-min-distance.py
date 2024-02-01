from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and arr[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))
                
q.append((0, 0))
visited[0][0] = True
dist[0][0] = 0
bfs()
print(dist[n - 1][m - 1])