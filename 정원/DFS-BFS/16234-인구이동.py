# 16234번 - 인구 이동

from collections import deque

n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue.append((x, y))
    union = [(x, y)]
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n or visited[nx][ny] == 1:
                continue
            # 연합 여부 확인
            if l <= abs(countries[a][b] - countries[nx][ny]) <= r:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                union.append((nx, ny))
    if len(union) <= 1:  # 연합이 될 수 없을 때까지
        return 0

    # 인구수 재계산
    res = sum(countries[a][b] for a, b in union) // len(union)
    for a, b in union:
        countries[a][b] = res
    return 1


# 날짜 계산
count = 0
while True:
    union_num = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union_num += bfs(i, j)
    if union_num == 0:
        break
    count += 1

print(count)
