n = int(input())
arr = []
for _ in range(n):
	arr.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
result = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for x in range(n):
    for y in range(n):
        cnt = 0
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if in_range(nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            result += 1
            
print(result)