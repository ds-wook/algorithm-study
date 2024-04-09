'''
교실의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)이다.
선생님은 학생의 순서를 정했고, 각 학생이 좋아하는 학생 4명도 모두 조사했다

한 칸에는 학생 한 명의 자리만 있을 수 있고, |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다고 한다.

1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
'''

import sys

input=sys.stdin.readline

score=[0,1,10,100,1000]

n=int(input().rstrip())

favorite={}
for i in range(1, n**2+1):
    favorite[i]=0 # 선호하는 학생이 없을 수도
    
seat=[[0 for _ in range(n)] for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

for _ in range(n**2):
    student=list(map(int, input().rstrip().split())) 
    favorite[student[0]]=student[1:]
    total=[]

    for x in range(n):
        for y in range(n):        
            
            if seat[x][y]!=0: # 이미 채워진 곳은 패스
                continue # 다시 for문 시작으로
            
            # 빈칸, 선호 학생 갯수 계산
            empty_cnt=0
            like_cnt=0
                
            for i in range(4): # 주변 확인
                nx=x+dx[i]
                ny=y+dy[i]
                        
                if (0<=nx<n) and (0<=ny<n):
                    if seat[nx][ny]==0:
                        empty_cnt+=1
                    if seat[nx][ny] in student[1:]:
                        like_cnt+=1
        
            total.append([empty_cnt, like_cnt, [x,y]])
    total.sort(key=lambda x:(-x[1], -x[0], x[2])) ######## like_cnt 큰 순서대로, empty_cnt 큰 순서대로, 나머지 // key, lambda로 정렬 가능
    # (배열이 복잡해지면) 시간 복잡도 클 수 있다 -> if문으로 처리 가능 
        
    seat[total[0][2][0]][total[0][2][1]]=student[0] # like 많고, empty 많은 곳에 student 배치

total_prefer=[0,0,0,0,0] # 만족도 0,1,2,3,4
 
### 만족도 계산하기
for x in range(n):
    for y in range(n):
        
        prefer=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if (0<=nx<n) and (0<=ny<n):
                if seat[nx][ny] in favorite[seat[x][y]]:
                    prefer+=1
        total_prefer[prefer]+=1

print(sum([total_prefer[i]*score[i] for i in range(5)]))
