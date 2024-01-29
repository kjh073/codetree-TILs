k, n = map(int, input().split())
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(pos):
    if pos == n + 1:
        print_answer()
        return
    
    for i in range(1, k + 1):
        if pos >= 3 and answer[-1] == i and answer[-2] == i:
            continue   
        answer.append(i)
        choose(pos + 1)
        answer.pop()
    return

choose(1)