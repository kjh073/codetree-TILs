n = int(input())
MAX_N = 1000

dp = [0] * (MAX_N + 1)
dp[0], dp[1], dp[2], dp[3] = 0, 0, 1, 1

for i in range(4, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 3])

# print(dp)
print(dp[n] % 10007)