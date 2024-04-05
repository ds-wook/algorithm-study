""" 
인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

"""
## => 이어서 풀기

import sys
from collections import deque

input=sys.stdin.readline

n,l,r=list(map(int, input().split()))

a=[list(map(int, input().split())) for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]
    

def bfs():
    q=deque()
    cnt=0
    
    while q:
        x,y=q.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if (nx>=0 and nx<2) and (ny>=0 and ny<2) and united[nx][ny]==0:
                q.append([nx,ny])
                cnt+=1
                united[i][j]=0
    
    for i in range(n):
        for j in range(n):
            if union[i][j]!=0:
                a[i][j]=sum(union)//cnt


union=[[0 for _ in range(n)] for _ in range(n)]
united=[[1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if l<=a[i][j] and a[i][j]<r:
            bfs()