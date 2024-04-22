'''
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 
이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
'''

import sys

# input=sys.stdin.readline

# n,x=map(int, input().rstrip().split())
# element=list(map(int, input().rstrip().split()))

#### ver1
# if x not in element:
#     print(-1)
# else:
#     print(element.count(x))

#### ver2
# start=0
# end=len(element)-1
# total=0

# while start<=end:
#     mid=(start+end)//2
    
#     if element[mid]==x:
#         for i in range(mid, -1, -1): # [3,2,1,0]
#             if element[i]==x:
#                 total+=1
#             else:
#                 break
#         for i in range(mid+1, len(element)): # [4,5,6]
#             if element[i]==x:
#                 total+=1
#             else:
#                 break
#         break
#     elif element[mid]>=x:
#         start=mid-1
#     else:
#         end=mid+1

# if total==0:
#     print(-1)
# else:
#     print(total)
    

### ver3

# x의 첫 번째 위치 구하기
def bs_start(element, target, start, end):
    while start<=end:
        mid=(start+end)//2
        if element[mid]==target:
            if mid-1<0 or element[mid-1]!=target: # 이전 값이 없거나, 이전 값이 다름
                return mid
            else: # 이전 값이 target
                end=mid-1 
        elif element[mid]>=target: # end를 mid-1로
            end=mid-1
        else: # start를 mid+1로 당기기
            start=mid+1
    return -1

# x의 마지막 위치 구하기
def bs_end(element, target, start, end):
    while start<=end:
        mid=(start+end)//2
        if element[mid]==target:
            if mid+1>len(element) or element[mid+1]!=target: # 이전 값이 없거나, 이전 값이 다름
                return mid
            else: # 이전 값이 target
                end=mid-1 
        elif element[mid]>=target: # end를 mid-1로
            end=mid-1
        else: # start를 mid+1로 당기기
            start=mid+1
    return -1

if __name__=="__main__":
    input=sys.stdin.readline

    n,x=map(int, input().rstrip().split())
    element=list(map(int, input().rstrip().split()))
    
    start=0
    end=len(element)-1
    total=0
    
    if bs_start(element, x, 0, len(element)-1) == -1 : # 존재하지 않음
        print(-1)
    else: # start 존재시 (start~end까지 갯수 계산)
        print(bs_end(element, x, 0, len(element)-1) - bs_start(element, x, 0, len(element)-1) + 1)