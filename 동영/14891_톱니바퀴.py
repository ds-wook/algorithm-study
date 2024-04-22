"""
총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 아래 그림과 같이 일렬로 놓여져 있다. 또, 톱니는 N극 또는 S극 중 하나를 나타내고 있다. 
톱니바퀴에는 번호가 매겨져 있는데, 가장 왼쪽 톱니바퀴가 1번, 그 오른쪽은 2번, 그 오른쪽은 3번, 가장 오른쪽 톱니바퀴는 4번이다.
톱니바퀴를 총 K번 회전시키려고 한다.
회전은 시계 방향과 반시계 방향

톱니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 최종 톱니바퀴의 상태를 구하는 프로그램을 작성하시오.

12시방향부터 시계방향 순서대로 주어진다. N극은 0, S극은 1로 나타나있다.

"""

import sys
from collections import deque

input = sys.stdin.readline

gear = [deque(input().rstrip()) for _ in range(4)]

k = int(input().rstrip())
rotate_gear_direction = [list(map(int, input().rstrip().split())) for _ in range(k)]


for i in range(k):
    # print(i)
    gear_num, gear_direction = rotate_gear_direction[i]

    rotate_gear = [0 for _ in range(4)]
    rotate_gear[gear_num - 1] = 1
    if gear_num % 2 == 0:
        direction = [-1, 1, -1, 1]
    else:
        direction = [1, -1, 1, -1]

    ## N-S극인 톱니바퀴 회전 ((-1)*(gear_direction))
    # 회전하는 톱니바퀴 찾기
    for j in range(gear_num - 1, 0, -1):
        if gear[j][6] != gear[j - 1][2]:
            rotate_gear[j - 1] = 1
        else:
            break

    for j in range(gear_num - 1, 4 - 1):
        if gear[j][2] != gear[j + 1][6]:
            rotate_gear[j + 1] = 1
        else:
            break

    # 회전하기
    for j, r in enumerate(rotate_gear):
        gear[j].rotate(r * direction[j] * gear_direction)

score = [1, 2, 4, 8]
result = [int(gear[i][0]) * score[i] for i in range(4)]
print(sum(result))
