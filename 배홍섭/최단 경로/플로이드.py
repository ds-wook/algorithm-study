N=5
M=14
edges = [
[1, 2, 2],
[1, 3, 3],
[1, 4, 1],
[1, 5, 10],
[2, 4, 2],
[3, 4, 1],
[3, 5, 1],
[4, 5, 3],
[3, 5, 10],
[3, 1, 8],
[1, 4, 2],
[5, 1, 7],
[3, 4, 2],
[5, 2, 4],
]

N=int(input())
M=int(input())
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))

INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

for start,end,cost in edges:
    graph[start][end]=min(graph[start][end],cost)
    
for i in range(N+1): #자기자신 거리는 0
    graph[i][i]=0
    
for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            
for row in graph[1:]:
    for value in row[1:]:
        print(0 if value==INF else value, end=' ')
    print()