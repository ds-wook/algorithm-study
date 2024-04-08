N,M = 5,3
graph = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]

N,M = 5,2
graph = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2 ,2, 0, 1, 2],
]

N,M = 5,1
graph = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
]

N,M = 5,1
graph = [
    [1, 2, 0, 2, 1],
    [1, 2, 0, 2, 1],
    [1, 2 ,0, 2, 1],
    [1, 2 ,0, 2, 1],
    [1, 2 ,0, 2, 1],
]

N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

chickens,houses = [],[]
for r,row in enumerate(graph):
    for c,value in enumerate(row):
        if value==1:
            houses.append([r,c])
        if value==2:
            chickens.append([r,c])
            

candidates = []
def combinations(n,new_arr,c):
    global chickens
    if len(new_arr)==n:
        candidates.append(new_arr)
        return new_arr
    for i in range(c,len(chickens)):
        combinations(n,new_arr+[chickens[i]],i+1)

# import math # 치킨집은 최대 13개. 그 중에 6개를 뽑는 경우의 수가 가장 많음
# print(math.factorial(13)/(math.factorial(6)*math.factorial(7))) #최대 1716개
combinations(M,[],0)

answer = int(1e9)
for candidate in candidates:
    value = 0
    for hr,hc in houses:
        value+=min([abs(hr-cr)+abs(hc-cc) for cr,cc in candidate])
    answer=min(answer,value)
    
print(answer)