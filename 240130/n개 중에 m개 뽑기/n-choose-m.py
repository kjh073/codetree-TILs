n, m = map(int, input().split())
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(pos, n_num):
    if pos == m + 1:
        # if pos == m:
        print_answer()
        return
    
    for i in range(n_num, n + 1):
        # if pos >= 3 and answer[-1] == i and answer[-2] == i:
        #     continue
         
        answer.append(i)
        choose(pos + 1, i + 1)
        answer.pop()
    return

choose(1, 1)