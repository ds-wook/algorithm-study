N = 3 # 2 <= N <= 125 탐사 공간의 크기(N*N)
graph = [
    [5,5,4],
    [3,9,1],
    [3,2,7]
]

N = 5 # 2 <= N <= 125 탐사 공간의 크기(N*N)
graph = [
    [3,7,2,0,1],
    [2,8,0,9,1],
    [1,2,1,8,1],
    [9,8,9,2,0],
    [3,6,5,1,5]
]

N = 7 # 2 <= N <= 125 탐사 공간의 크기(N*N)
graph = [
    [9,0,5,1,1,5,3],
    [4,1,2,1,6,5,3],
    [0,7,6,1,6,8,5],
    [1,1,7,8,3,2,3],
    [9,4,0,7,6,4,1],
    [5,8,3,2,4,8,3],
    [7,4,8,4,8,3,4]
]

import heapq

INF = int(1e9)
dp_table = [[INF]*N for _ in range(N)]
dp_table[0][0]=graph[0][0]

heap = [[graph[0][0],0,0]]
heapq.heapify(heap)

drow,dcolumn=[0,-1,0,1],[1,0,-1,0] #우상좌하

while heap:
    cost,row,column = heapq.heappop(heap)
    for i in range(4):
        n_row,n_column = row+drow[i], column+dcolumn[i]
        if 0<=n_row<N and 0<=n_column<N:
            if cost+graph[n_row][n_column] < dp_table[n_row][n_column]:
                dp_table[n_row][n_column]=cost+graph[n_row][n_column]
                heapq.heappush(heap,[cost+graph[n_row][n_column],n_row,n_column])

for row in dp_table:
    print(row)
    
print(dp_table[-1][-1])