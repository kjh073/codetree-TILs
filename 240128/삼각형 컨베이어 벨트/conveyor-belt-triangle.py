n, t = map(int, input().split())
fir = list(map(int, input().split()))
sec = list(map(int, input().split()))
tri = list(map(int, input().split()))

def change_num():
    fir_e = fir[n - 1]
    sec_e = sec[n - 1]
    tri_e = tri[n - 1]
    for i in range(n - 1, 0, -1):
        fir[i] = fir[i - 1]
        sec[i] = sec[i - 1]
        tri[i] = tri[i - 1]
    fir[0] = tri_e
    sec[0] = fir_e
    tri[0] = sec_e
    
for i in range(t):
    change_num()
    
for i in range(n):
    print(fir[i], end=" ")
print()

for i in range(n):
    print(sec[i], end=" ")
print()

for i in range(n):
    print(tri[i], end=" ")
print()