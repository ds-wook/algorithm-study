'''
실패율은 다음과 같이 정의한다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

'''

def solution(N, stages):
    
    # stages.sort()
    length=len(stages)
    fail=[]
    for i in range(1,N+1):
        
        cnt=stages.count(i)
        
        if length==0: # 도중에 모든 player가 탈락한 경우
            fail.append((i,0))
        else:
            fail.append((i,cnt/length))
        
        length-=cnt
    
    # print(sorted(fail, key=lambda x:x[1], reverse=True))
    
    answer=[x[0] for x in sorted(fail, key=lambda x:x[1], reverse=True)]
    return answer


        # print(sorted(fail.items(), key=lambda x:-x[0]))
    # answer=[]
    # for a,b in sorted(fail.items(), key=lambda x:-x[0]):
    #     answer.extend(b)
        # print(fail.keys()[list(fail.items()).index(i)-1])
        # answer.extend(i)
    
    # answer = [j for i in sorted(fail, reverse=True) for j in fail[i]]
    

#     for i in range(1,N+1):      
#         s=stages[0]
#         if s==N+1:    
#             break
#         else:    
#             # if stages.count(s)/len(stages) in fail.keys():
#             #     fail[stages.count(s)/len(stages)].append(s)
#             # else:
#             #     fail[stages.count(s)/len(stages)]=[s]
#             if answer==0:
#                 answer.append()
#             fail[s]=stages.count(s)/len(stages)
            
#             for _ in range(stages.count(s)):
#                 stages.pop(0)
    
    # answer=[]
    # for a,b in sorted(fail.items(), key=lambda x:-x[0]):
    #     answer.extend(b)
        # print(fail.keys()[list(fail.items()).index(i)-1])
        # answer.extend(i)
    
    # answer = [j for i in sorted(fail, reverse=True) for j in fail[i]]