from collections import deque
import sys

DFS_result = []

# 재귀
def DFS(graph, node, visited):
    if node not in visited:
        visited.add(node)
        DFS_result.append(node)
        for i in sorted(graph[node]):
            DFS(graph, i, visited)

    return DFS_result

BFS_result = []

# 큐
def BFS(graph, start, visited):

    BFS_queue = deque([start])

    while BFS_queue:
        node = BFS_queue.popleft()
        if node not in visited:
            visited.add(node)
            BFS_result.append(node)
            BFS_queue.extend(sorted(graph[node]))

    return BFS_result
  
  
N, M, V = map(int, sys.stdin.readline().split())


graph = {i: [] for i in range(1, int(N)+1)}

for i in range(int(M)):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()
DFS(graph, V, visited)
print(*DFS_result)

visited = set()
BFS(graph, V, visited)
print(*BFS_result)