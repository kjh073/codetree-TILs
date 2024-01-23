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
		dir_num = dir_num

x += dx[dir_num]
y += dy[dir_num]

print(x, y)