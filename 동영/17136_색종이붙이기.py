'''
정사각형 모양을 한 다섯 종류의 색종이가 있다. 색종이의 크기는 1×1, 2×2, 3×3, 4×4, 5×5로 총 다섯 종류가 있으며, 각 종류의 색종이는 5개씩 가지고 있다.

색종이를 크기가 10×10인 종이 위에 붙이려고 한다. 
종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 0 또는 1이 적혀 있다. 1이 적힌 칸은 모두 색종이로 덮여져야 한다. 
색종이를 붙일 때는 종이의 경계 밖으로 나가서는 안되고, 겹쳐도 안 된다. 또, 칸의 경계와 일치하게 붙여야 한다. 
0이 적힌 칸에는 색종이가 있으면 안 된다.

종이가 주어졌을 때, 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수를 구해보자.
'''

import sys

input=sys.stdin.readline
graph=[list(map(int, input().split())) for _ in range(10)]
paper=[0,5,5,5,5,5]

result=set() ## list로 두면 시간초과 발생 -> set으로 하면 성공 (set은 ~.add()로 원소 추가)


def cover(i,j,l):
    for k in range(i,i+l):
        for m in range(j,j+l):
            graph[k][m]=0

def uncover(i,j,l):
    for k in range(i,i+l):
        for m in range(j,j+l):
            graph[k][m]=1
            
def find_papeLength(x,y):
    length=1
    for l in range(2, min(10-x, 10-y,5)+1): # 1x1부터 최대 5x5까지 / range(1,~)이면 자기자신이니까 so range(2,~) 부터
        for i in range(x,x+l):
            for j in range(y,y+l): # range는 +1
                if graph[i][j]==0:
                    return length
        length+=1
    return length


def dfs(cnt):
   
    for i in range(10):
        for j in range(10):
            if graph[i][j]==1:
                length=find_papeLength(i,j)
                # print(f'length {length}')
                
                for l in range(length,0,-1): # 최대 length 크기만큼의 색종이 사용 가능
                    if paper[l]: # 가릴 종이가 있다면
                        paper[l]-=1
                        cover(i,j,l) # 가리기 
                        result.add(dfs(cnt+1)) # 확인하기
                        uncover(i,j,l) # 지우기
                        paper[l]+=1
                
                if result:
                    return min(result)
                else:
                    return -1
                
    return cnt            
           
result.add(dfs(0))

result=[i for i in result if i!=-1]
if result:
    print(min(result))
else:
    print(-1)
