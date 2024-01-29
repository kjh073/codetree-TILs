turn, fin, mark = map(int, input().split())
move = list(map(int, input().split()))
answer = []
max_mark = 0

def move_mark():
    global max_mark
    move_cnt = [0] * (mark + 1)
    fin_mark = 0
    for i in range(turn):
        move_cnt[answer[i]] += move[i]
    for i in move_cnt:
        if i >= fin:
            fin_mark += 1
    max_mark = max(max_mark, fin_mark)
    # print(move_cnt)

def choose(pos):
    if pos == turn + 1:
        move_mark()
        return
    
    for i in range(1, mark + 1):
        answer.append(i)
        choose(pos + 1)
        answer.pop()
    return

choose(1)
print(max_mark)