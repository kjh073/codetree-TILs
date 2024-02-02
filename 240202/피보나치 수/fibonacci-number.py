n = int(input())
fibo = [-1] * (n + 1)

for i in range(1, n + 1):
    if i == 1 or i == 2:
        fibo[i] = 1
    else:
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    
print(fibo[n])