import sys
sys.stdin = open('input.txt','r')

def find_parent(parent, x):
	# 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출 
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

N = int(input())
parent = [i for i in range(N+1)] # 부모 테이블 초기화

"""	
graph = []
for _ in range(N):
	graph.append(list(map(int, input().split())))
      
combi = list(combinations([i for i in range(N)], 2))
edges = []
for c1,c2 in combi:
	cost = min(abs(graph[c1][0]-graph[c2][0]), abs(graph[c1][1]-graph[c2][1]), abs(graph[c1][2]-graph[c2][2]))
	edges.append((cost, c1,c2))
edges.sort()
"""

# x,y,z 축에 대하여 정렬 이후에 3x(N-1)개의 간선에 대해 최소 비용
x = []
y = []
z = []

for i in range(1,N+1):
    data = list(map(int, input().split()))
    x.append((data[0], i)) #좌표, 인덱스
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(N-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))
# 간선을 비용순으로 정렬
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
print(result)