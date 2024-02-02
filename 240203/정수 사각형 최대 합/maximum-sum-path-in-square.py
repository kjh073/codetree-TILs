# import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# max_num = -sys.maxsize
dp = [[-1 for _ in range(n)] for _ in range(n)]

def initialize():
    dp[0][0] = arr[0][0]
    
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + arr[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + arr[0][j]
                
initialize()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]
        # print(i, j, dp)

# for j in range(n):
#     max_num = max(dp[n - 1][j])
print(dp[n - 1][n - 1])