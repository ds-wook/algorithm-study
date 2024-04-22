import sys
from collections import deque

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, k = map(int, input().split())
con = deque(list(map(int, input().split())))
cnt = 0
robot = deque([0] * n)
while True:
    cnt += 1
    # 1. 벨트 회전
    con.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    # 2. 로봇 한칸 이동
    for i in range(n - 2, -1, -1):  # 먼저 올린 로봇부터 진행
        if robot[i] == 1 and robot[i + 1] == 0 and con[i + 1] >= 1:
            robot[i] = 0
            robot[i + 1] = 1
            con[i + 1] -= 1
    robot[-1] = 0
    # 3. 로봇 올리기
    if con[0] > 0:
        con[0] -= 1
        robot[0] = 1
    # 4. 종료
    if con.count(0) >= k:
        break
print(cnt)
