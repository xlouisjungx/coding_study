import sys

# 런타임 에러 (RecursionError) --> 재귀 호출이 너무 깊어져서 발생하는 에러, 최대 재귀 깊이를 설정해야함.
sys.setrecursionlimit(10**6)

DFS_result = []

# 재귀
def DFS(graph, node, visited):
    if node not in visited:
        visited.add(node)
        DFS_result.append(node)

        for i in sorted(graph[node]):
            
            DFS(graph, i, visited)

N, M = map(int, sys.stdin.readline().split())

graph = {i: [] for i in range(1, N+1)}
visited = set()
cnt = 0

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for node in range(1, N+1):
    if node not in visited:
        cnt += 1
        DFS(graph, node, visited)

print(cnt)