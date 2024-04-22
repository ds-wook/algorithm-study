'''
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오
'''
import sys

if __name__=="__main__":
    input=sys.stdin.readline
    
    n,c=map(int, input().rstrip().split())
    
    home=[int(input().rstrip()) for _ in range(n)]
    home.sort()
    
    start=1 # 최소 거리 
    end=home[-1]-home[0] # 최대 거리
    total=0
    
    while start<=end:
        
        mid=(end+start)//2 # 중간 거리
        
        current=home[0] # 앞집부터 설치
        cnt=1

        for i in range(1,len(home)): 
            if home[i]>=current+mid: # 마지막으로 설치한 공유기와 거리가 mid 보다 클때
                cnt+=1 # 공유기 설치
                current=home[i]

        if cnt>=c: # 공유기 개수가 c개를 넘어가면
            start=mid+1 # 차이 키우기
            total=mid
        else: #  c개를 넘어가지 않는다면
            end=mid-1 # 차이 줄이기
            
    print(total)
    