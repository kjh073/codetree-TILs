n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def is_match_r(r):
    for j in range(n):
        cnt = 1
        for k in range(1, m):
            if in_range(i, j + k) and arr[r][j] == arr[r][j + k]:
                cnt +=1
            else:
                continue
        if cnt >= m:
            return 1
    return 0

def is_match_c(c):
    for i in range(n):
        cnt = 1
        for k in range(1, m):
            if in_range(i + k, j) and arr[i][c] == arr[i + k][c]:
                cnt +=1
            else:
                continue
        if cnt >= m:
            return 1
    return 0

for i in range(n):
    result += is_match_r(i)
for j in range(n):
    result += is_match_c(j)
print(result)