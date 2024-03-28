"""
연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
빈 칸의 개수는 3개 이상이다.
"""

import copy
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# bfs
def bfs():

    q = deque()
    temp = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append([i, j])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx >= 0 and nx < n) and (ny >= 0 and ny < m) and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append([nx, ny])

    global answer
    cnt = sum([temp[i].count(0) for i in range(n)])

    answer = max(answer, cnt)


def wall(cnt):  # 백트래킹: 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾아가는 기법
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1  # 세웠다가
                wall(cnt + 1)
                graph[i][j] = 0  # 허물기


answer = 0
wall(0)
print(answer)
