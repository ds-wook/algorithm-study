'''
격자의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)이다. 마법사 상어는 연습을 위해 1번 행과 N번 행을 연결했고, 1번 열과 N번 열도 연결했다. 
즉, N번 행의 아래에는 1번 행이, 1번 행의 위에는 N번 행이 있고, 1번 열의 왼쪽에는 N번 열이, N번 열의 오른쪽에는 1번 열이 있다.

비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다. 구름은 칸 전체를 차지한다. 이제 구름에 이동을 M번 명령하려고 한다. 
i번째 이동 명령은 방향 di과 거리 si로 이루어져 있다. 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현한다. 
1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다. 이동을 명령하면 다음이 순서대로 진행된다.

1. 모든 구름이 di 방향으로 si칸 이동한다.
2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
3. 구름이 모두 사라진다.
4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
    이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
    예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.

M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.
'''

import sys

input=sys.stdin.readline


n,m = map(int, input().rstrip().split())
graph=[list(map(int, input().rstrip().split())) for _ in range(n)]

ds=[list(map(int, input().rstrip().split())) for _ in range(m)]

cloud=[[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

dx=[ 0, -1,-1,-1, 0, 1, 1,  1]
dy=[-1, -1, 0, 1, 1, 1, 0, -1]

dx2=[1,1,-1,-1]
dy2=[-1,1,-1,1]


for d,s in ds:
    moved_cloud = []
    visited=[[False for _ in range(n)] for _ in range(n)] # visited 안 사용하면 시간 초과 발생
     
    for i in range(len(cloud)):
        new_x=(cloud[i][0]+dx[d-1]*s)%n
        new_y=(cloud[i][1]+dy[d-1]*s)%n
        
        # if new_x<0:
        #     new_x+=n
        # elif new_x>=n:
        #     new_x-=n
        
        # if new_y<0:
        #     new_y+=n
        # elif new_y>=n:
        #     new_y-=n
        moved_cloud.append([new_x,new_y])
        graph[new_x][new_y]+=1
        visited[new_x][new_y]=True
    
    for r,c in moved_cloud:
        cnt=0
        # 물복사버그 마법
        for k in range(4):
            if (0<=r+dx2[k]<n) and (0<=c+dy2[k]<n) and graph[r+dx2[k]][c+dy2[k]]>0:
                cnt+=1
        graph[r][c]+=cnt
    
    cloud=[]
    for i in range(n):
        for j in range(n):
            if graph[i][j]>=2 and not visited[i][j]: 
                cloud.append([i,j])
                graph[i][j]-=2

result=0
for i in range(n):
    result+=sum(graph[i])

print(result)
        