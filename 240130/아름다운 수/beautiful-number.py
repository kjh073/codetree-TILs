# n = int(input())
num = []
answer = []
n = 10
cnt = 0

def is_beautiful(num):
    max_num = 1
    for i in range(1, n):
        if num[i - 1] != 1 and num[i] == num[i - 1]:
            max_num += 1
        elif num[i - 1] != 1 and num[i] != num[i - 1]:
            if max_num != num[i - 1]:
                return False
            elif num[i - 1] == max_num:
                max_num = 1
    if max_num != num[n - 1]:
        return False
    return True         
            

def choose(pos):
    global cnt
    if pos == n + 1:
        if is_beautiful(num):
            cnt += 1
            # print(num)
        # print(is_beautiful(num))
        # print(answer)
        # print()
        # print(len(answer))
        return
    
    for i in range(1, n + 1):
        # if i != 1 and n - len(num) < i:
        #     return
        num.append(i)
        choose(pos + 1)
        num.pop()
    return

choose(1)
print(cnt)
# print(answer)
# num = [2, 2, 1]
# print(is_beautiful(num))