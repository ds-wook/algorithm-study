N, M = map(int, input().split())
virus_map = []
for _ in range(N):
    row = list(map(int,input().split()))
    virus_map.append(row)
    
# N,M = 7,7
# virus_map = [
#     [2,0,0,0,1,1,0],
#     [0,0,1,0,1,2,0],
#     [0,1,1,0,1,0,0],
#     [0,1,0,0,0,0,0],
#     [0,0,0,0,0,1,1],
#     [0,1,0,0,0,0,0],
#     [0,1,0,0,0,0,0],
# ]

# N,M = 4,6
# virus_map = [
#     [0,0,0,0,0,0],
#     [1,0,0,0,0,2],
#     [1,1,1,0,0,2],
#     [0,0,0,0,0,2]
# ]

# N,M = 8,8
# virus_map = [
#     [2,0,0,0,0,0,0,2],
#     [2,0,0,0,0,0,0,2],
#     [2,0,0,0,0,0,0,2],
#     [2,0,0,0,0,0,0,2],
#     [2,0,0,0,0,0,0,2],
#     [0,0,0,0,0,0,0,0],    
#     [0,0,0,0,0,0,0,0],    
#     [0,0,0,0,0,0,0,0],    
# ]

from itertools import combinations
from collections import deque
import copy

candidates = []
for row in range(N): #최대 8
    for column in range(M): #최대 8 -> 64번 반복.
        if virus_map[row][column] == 0:
            candidates.append([row,column])
            
candidates = list(combinations(candidates, 3)) #최대 64C3 = 41,664번.
#print(len(list(combinations([i for i in range(64)],3))))

answer = 0
for candidate in candidates:
    virus_map_copy = copy.deepcopy(virus_map)
    for row,column in candidate: #빈칸에 벽 설치
        virus_map_copy[row][column] = 1
    
    visited=[[False]*M for _ in range(N)]
    for row in range(N):
        for column in range(M):
            if not visited[row][column] and virus_map_copy[row][column]==2: #초기 바이러스가 존재하는 곳. 전파 시작
                dq = deque([[row,column]])
                
                while dq:
                    now_row, now_column = dq.popleft()
                    if visited[now_row][now_column]:
                        continue
                    else:
                        visited[now_row][now_column]=True
                        
                    if now_column+1<M and virus_map_copy[now_row][now_column+1]!=1: #오른쪽으로 바이러스가 퍼지는 경우
                        dq.append([now_row,now_column+1])
                        virus_map_copy[now_row][now_column+1]=2
                        
                    if now_row-1>=0 and virus_map_copy[now_row-1][now_column]!=1: #위쪽으로 바이러스가 퍼지는 경우
                        dq.append([now_row-1,now_column])
                        virus_map_copy[now_row-1][now_column]=2
                        
                    if now_column-1>=0 and virus_map_copy[now_row][now_column-1]!=1: #왼쪽으로 바이러스가 퍼지는 경우
                        dq.append([now_row,now_column-1])
                        virus_map_copy[now_row][now_column-1]=2
                        
                    if now_row+1<N and virus_map_copy[now_row+1][now_column]!=1: #아래로 바이러스가 퍼지는 경우
                        dq.append([now_row+1,now_column])
                        virus_map_copy[now_row+1][now_column]=2
                
    count = 0                    
    for x in virus_map_copy:
        count+=x.count(0)
    answer = max(answer, count)
print(answer)