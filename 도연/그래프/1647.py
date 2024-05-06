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

N, M = list(map(int, input().split()))
edges = []
for _ in range(M):
    a,b,cost = list(map(int, input().split()))
    edges.append((cost, a, b))

edges.sort()
parent = [i for i in range(N+1)] # 부모 테이블 초기화
result = 0
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a,b)
        result += cost
        last = cost
print(result - last)