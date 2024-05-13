import sys
from collections import deque
input = sys.stdin.readline
t = [deque(list(map(int,input().rstrip()))) for _ in range(4)] # 톱니 상태 저장
k = int(input())
for _ in range(k):
    r,d = map(int, input().split())
    r -= 1 #톱니번호를 0부터 3으로 만들기 위해
    q = deque([[r,d,0]])
    while q:
        r,d,lr = q.popleft()
        
        # 왼쪽 확인 (idx = 2)
        if 0 <= r-1 and t[r-1][2] != t[r][6] and lr != 1:
            q.append([r-1, -d, -1])
        # 오른쪽 확인 (idx = 6)
        if r+1 < 4 and t[r+1][6] != t[r][2] and lr != -1:
            q.append([r+1, -d, 1])

        # 회전
        if d == 1: #시계
            t[r].appendleft(t[r].pop())
        elif d == -1: #반시계
            t[r].append(t[r].popleft())

cnt = 0
for i in range(4):
    if t[i][0] == 1:
        cnt += 2**i
print(cnt)