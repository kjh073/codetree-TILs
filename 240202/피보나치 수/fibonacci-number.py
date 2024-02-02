n = int(input())
memo = [-1] * (n + 1)

def fibo(i):
    if memo[i] != -1:
        return memo[i]
    if i == 1 or i == 2:
        memo[i] = 1
    else:
        memo[i] = fibo(i - 1) + fibo(i - 2)
    return memo[i]
    
fibo(n)
print(memo[n])