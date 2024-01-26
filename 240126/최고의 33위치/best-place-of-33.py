# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]
max_coin = 0
n = 3
grid = [[1, 0, 1], [0, 1, 0], [0, 1, 0]]

def num_gold(r, c):
    cnt = 0
    for i in range(r + 3):
        for j in range(c + 3):
            if grid[i][j] == 1:
                cnt += 1
    return cnt

for r in range(n):
    for c in range(n):
        if r + 2 >= n or c + 2 >= n:
            continue
        curr_coin = num_gold(r, c)
        max_coin = max(curr_coin, max_coin)

print(max_coin)