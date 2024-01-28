n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k -= 1

def able_row(r, row):
    for j in range(0, m):
        if row[k + j] != 0:
            return False
    return True
    
drop_row = 0
for i in range(n):
    if able_row(i, arr[i]):
        drop_row = i

for j in range(0, m):
    arr[drop_row][k + j] = 1

for r in range(n):
    for c in range(n):
        print(arr[r][c], end=" ")
    print()