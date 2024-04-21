N,M = 3,3
r,c,d = 1,1,0 
graph = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]

N,M = 11,10
r,c,d = 7,4,0 
graph = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0 ,0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0 ,0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0 ,1, 0, 1],
    [1, 0, 0, 0 ,0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0 ,0 ,0, 1, 1, 0, 1],
    [1, 0, 0, 0 ,0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1 ,1, 1, 1, 1, 1, 1],
]

N,M = map(int, input().split())
r,c,d = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))


from collections import deque

'''
    direction: 0,1,2,3 순서대로 북,동,남,서(시계방향)
'''

def forward(graph,row,column,direction):
    try:
        if direction==0:
            return graph[row-1][column]==0
        elif direction==1:
            return graph[row][column+1]==0
        elif direction==2:
            return graph[row+1][column]==0
        else:
            return graph[row][column-1]==0
    
    except:
        return False

dq = deque([[r,c,d]])
count=0
while dq:
    #print(dq)
    row,column,direction = dq.pop()

    if graph[row][column]==0:
        graph[row][column]=2
        count+=1
    
    available = False
    for i in range(4):
        direction = (direction-1)%4
        if forward(graph,row,column,direction):
            available=True
            if direction==0:
                dq.append([row-1,column,direction])
            elif direction==1:
                dq.append([row,column+1,direction])
            elif direction==2:
                dq.append([row+1,column,direction])
            else:
                dq.append([row,column-1,direction])
                
            break
        
    if available: #전진 가능한 경우
        continue
    
    #4방향 모두 탐색했는데 청소되지 않은 빈 칸이 없는 경우
    try:
        if direction==0:
            if graph[row+1][column]==1:
                break
            else:
                dq.append([row+1,column,direction])
        elif direction==1:
            if graph[row][column-1]==1:
                break
            else:
                dq.append([row,column-1,direction])
        elif direction==2:
            if graph[row-1][column]==1:
                break
            else:
                dq.append([row-1,column,direction])
        else:
            if graph[row][column+1]==1:
                break
            else:
                dq.append([row,column+1,direction])
    except:
        break
    
print(count)