n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2)]

def change_position():
    tmp1 = arr[0][n - 1]
    tmp2 = arr[1][n - 1]
    for r in range(1, -1, -1):
        for c in range(n - 1, 0, -1):
            arr[r][c] = arr[r][c - 1]
        if r == 0:
            arr[r][0] = tmp2
        else:
            arr[r][0] = tmp1
                
for i in range(t):
    change_position()
    
for r in range(2):
    for c in range(n):
        print(arr[r][c], end=" ")
    print()