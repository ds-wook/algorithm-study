N, M = 6,7 # 1 <= N <= 20000 노드 수 | 1 <= M <= 50000 간선 수
edges = [
    [3,6],
    [4,3],
    [3,2],
    [1,3],
    [1,2],
    [2,4],
    [5,2],
]

from collections import deque

INF = int(1e9)
distances = [INF]*(N+1)

graph = [[] for _ in range(N+1)]
for start,end in edges:
    graph[start].append(end)
    graph[end].append(start)

distance=0
dq = deque([1])
while dq:
    n_dq = deque([])
    
    for neighbor in dq:
        if distances[neighbor] > distance:
            distances[neighbor]=distance
            n_dq.extend(graph[neighbor])
    
    distance+=1
    dq=n_dq
    
distances = distances[1:] #헛간 번호는 1번부터
print(distances)
max_value = max(distances)
index = distances.index(max_value)
print(index+1, distances[index], distances.count(distances[index]))