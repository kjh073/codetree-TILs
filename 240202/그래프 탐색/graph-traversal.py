n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

def dfs(vertex):
    for curr_v in graph[vertex]:
        if not visited[vertex]:
            print(curr_v)
            visited[vertex] = True
            dfs(curr_v)

for start, end in arr:
    graph[start].append(end)
    graph[end].append(start)

# root_vertex = 1
# visited[root_vertex] = True
# print(root_vertex)
# dfs(root_vertex)
print(len(graph[1]))