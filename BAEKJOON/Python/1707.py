from collections import deque
import sys



result = []

def BFS(graph, start):

    color = [-1] * (start + 1) # 색상 배열 (-1: 미방문, 0: 색1, 1: 색2)

    for i in range(1, start+1):
        if color[i] == -1: # 방문하지 않은 노드에서 BFS 시작
            q = deque([i])
            color[i] = 0 # 첫 노드 색상

            while q:
                node = q.popleft()
                for j in graph[node]:
                    if color[j] == -1: # 방문하지 않았다면 다른 색으로 칠함
                        color[j] = 1 - color[node]
                        q.append(j)
                    elif color[j] == color[node]: # 인접 노드가 같은 색이면 이분 그래프 아님
                        return "NO"
                    
    return "YES"


K = int(input()) # 테스트 케이스의 개수

for i in range(K):
    V, E = map(int, sys.stdin.readline().strip().split()) # 그래프의 정점 개수 / 간선의 개수

    graph = {i: [] for i in range(V+1)}

    for j in range(E):
        u, v = map(int, sys.stdin.readline().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    result.append(BFS(graph, V))

for i in range(len(result)):
    print(result[i])