n = int(input())
answer = []
visited = [False] * (n + 1)

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(pos):
    if pos == n + 1:
        print_answer()
        return
    
    for i in range(n, 0, -1):
        if visited[i] == True:
            continue
        visited[i] = True
        answer.append(i)
        choose(pos + 1)
        answer.pop()
        visited[i] = False
    return

choose(1)