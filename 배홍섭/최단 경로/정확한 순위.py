N,M = 6,6
edges = [
    [1,5],
    [3,4],
    [4,2],
    [4,6],
    [5,2],
    [5,4],
]

INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

for a,b in edges:
    graph[a][b]=1
    
for i in range(1,N+1):
    graph[i][i]=0
    
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

answer=0
for i in range(1,N+1):
    count=0
    for j in range(1,N+1):
        if graph[i][j]!=INF or graph[j][i]!=INF:    count+=1 #들어오는 간선의 개수 + 나가는 간선의 개수가 n이라면 정확한 순위를 알 수 있는 경우.
    if count==N:    answer+=1
    
print(answer)