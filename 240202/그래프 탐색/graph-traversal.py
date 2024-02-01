n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
cnt =  0

def dfs(vertex):
    global cnt
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            cnt += 1
            visited[curr_v] = True
            dfs(curr_v)

for start, end in arr:
    graph[start].append(end)
    graph[end].append(start)

root_vertex = 1
visited[root_vertex] = True
dfs(root_vertex)

print(cnt)