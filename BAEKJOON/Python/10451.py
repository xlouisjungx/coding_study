import sys

sys.setrecursionlimit(10**6)

def DFS(graph, node, visited, path):
    if node in path: # 현재 탐색 중인 경로에서 다시 방문 --> 사이클 발견
        return True
    if node in visited: # 이미 확인된 노드라면 건너뛴다.
        return False
    
    path.add(node) # 현재 탐색 중인 경로에 추가
    visited.add(node) # 방문 처리

    next_node = graph[node][0] # 주어진 문제에서 각 노드는 한 개의 간선만 가짐
    if DFS(graph, next_node, visited, path):
        return True
    
    path.remove(node) # 탐색이 끝난 후 제거
    return False

T = int(input()) # 테스트 케이스


result = []

for i in range(T):
    cnt = 0

    N = int(input()) # 순열의 크기
    num = list(map(int, sys.stdin.readline().strip().split()))
    
    graph = {i + 1: [num[i]] for i in range(N)}
    visited = set()
    
    


    for node in range(1, N+1):
        if node not in visited:
            if DFS(graph, node, visited, set()): # 사이클이 있다면 개수 증가
                cnt += 1
    
    result.append(cnt)

for i in range(len(result)):
    print(result[i])