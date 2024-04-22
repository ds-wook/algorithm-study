"""
로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북 중 하나이다. 

로봇 청소기는 다음과 같이 작동한다.

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    3-1. 반시계 방향으로 90도 회전한다.
    3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    3-3. 1번으로 돌아간다.
"""

import sys

input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
x, y, d = list(map(int, input().rstrip().split()))
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

cleaned = [[0 for _ in range(m)] for _ in range(n)]
cleaned[x][y] = 1
cleaning = 1

while True:

    flag = 0
    for _ in range(4):
        # 시계 반대방향으로 회전
        nx = x + move[(d + 3) % 4][0]
        ny = y + move[(d + 3) % 4][1]
        d = (d + 3) % 4
        if (
            (0 <= nx and nx < n) and (0 <= ny and ny < m) and graph[nx][ny] == 0 and cleaned[nx][ny] == 0
        ):  # 앞쪽이 청소되지 않은 칸
            cleaned[nx][ny] = 1
            cleaning += 1
            x = nx
            y = ny
            flag = 1  # 한 곳이라도 청소 함
            break

    if flag == 0:
        # 뒤쪽 방향
        # 벽이면 STOP
        if graph[x - move[d][0]][y - move[d][1]] == 1:
            print(cleaning)
            break
        else:  # 후진
            x -= move[d][0]
            y -= move[d][1]
