N,K = 3,2
belts= [1,2,1,2,1,2]

N,K = 3,6
belts= [10,10,10,10,10,10]

N,K = 4,5
belts= [10,1,10,6,3,4,8,2]

N,K = 5,8
belts= [100,99,60,80,30,20,10,89,99,100]

N,K = map(int,input().split())
belts = list(map(int,input().split()))


from collections import deque

count=belts.count(0)
robots = deque() #로봇의 위치를 담는 배열. index형식으로 belts의 index를 의미
now = 0 
while count<K:
    #print(belts[:N],robots)
    now+=1 # 가장 처음 수행되는 단계는 1번째 단계
    
    #step1 벨트와 로봇 함께 회전
    belts = [belts[-1]] + belts[:-1]
    robots = deque([i+1 for i in robots if i!=N-1]) #한칸 회전
    
    #step2 로봇 이동
    number_of_robots = len(robots)
    for _ in range(number_of_robots):
        robot = robots.popleft()
        if robot==N-1:
            continue
        
        if (robot+1 not in robots) and belts[robot+1]>=1: #앞에 로봇이 없고 그 칸의 내구도가 1이상인 경우
            belts[robot+1]-=1 #내구도 1 감소
            if robot+1==N-1: #마지막에 도착하면 내림
                continue
            else:
                robots.append(robot+1) #로봇 한칸 이동
        else: #이동 안하는 경우
            robots.append(robot)
                
    #step3 로봇 올리기
    if belts[0]>0:
        robots.append(0)
        belts[0]-=1
    
    #step4 내구도가 0인 칸의 개수 세기
    count=belts.count(0)

print(now)