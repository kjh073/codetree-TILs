import sys

INT_MIN = -sys.maxsize

n = int(input())
dp = [0] * n
arr = list(map(int, input().split()))

def initialize():
    for i in range(n):
        dp[i] = INT_MIN
    dp[0] = 1

initialize()
    
for i in range(1, n):
    for j in range(i):
        if dp[j] == INT_MIN:
            continue
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
result = 0
for i in range(n):
    result = max(result, dp[i])
# print(dp)
print(result)