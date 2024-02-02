import sys

INT_MAX = sys.maxsize

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[INT_MAX for _ in range(n)] for _ in range(n)]

def initialize():
    dp[0][n - 1] = arr[0][n - 1]
    
    for i in range(1, n):
        dp[i][n - 1] = dp[i - 1][n - 1] + arr[i][n - 1]
    for j in range(n - 2, -1, -1):
        dp[0][j] = dp[0][j + 1] + arr[0][j]
                
initialize()

for i in range(1, n):
    for j in range(n - 2, -1, -1):
        dp[i][j] = min(dp[i - 1][j], dp[i][j + 1]) + arr[i][j]
# print(dp)

print(dp[n - 1][0])