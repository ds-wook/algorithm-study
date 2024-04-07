# 14502번 - 연구소

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 0의 위치 저장
zero_position = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_position.append((i, j))

# 벽 조합 만들기
from itertools import combinations

wall_combs = combinations(zero_position, 3)

# 최대 safe 개수 구하기
max_safe = 0
for comb in wall_combs:
    new_graph = [row[:] for row in graph]
    for pos in comb:
        new_graph[pos[0]][pos[1]] = 1

    visited = [[0] * m for _ in range(n)]

    # dfs
    def dfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if new_graph[nx][ny] == 0 and visited[nx][ny] == False:
                new_graph[nx][ny] = 3
                dfs(nx, ny)

    # 2로부터 dfs
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 2:
                visited[i][j] = True
                dfs(i, j)

    # 0의 개수 세기(safe지역)
    curr_safe = 0
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 0:
                curr_safe += 1

    if curr_safe > max_safe:
        max_safe = curr_safe

print(max_safe)
