x, y = 0, 0
dir = input()
dir_num = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(len(dir)):
	if dir[i] == 'L':
		dir_num = (dir_num - 1 + 4) % 4
	elif dir[i] ==  'R':
		dir_num = (dir_num + 1) % 4
	elif dir[i] == 'F':
		x += dx[dir_num]
		y += dy[dir_num]
	if x == 0 and y == 0:
		print(i + 1)
		break

if x != 0 or y != 0:
    print(-1)