n = int(input())
arr = [int(input()) for i in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

tmp = [0] * n
idx = 0
for i in range(n):
    if not (s1 - 1) <= i <= (e1 - 1):
        tmp[idx] = arr[i]
        idx += 1

tmp2 = [0] * idx
idx2 = 0
for i in range(idx):
    if not (s2 - 1) <= i <= (e2 - 1):
        tmp2[idx2] = tmp[i]
        idx2 += 1
        
print(idx2)
for i in range(idx2):
    print(tmp2[i])