import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

wall = []
virus = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            wall.append([i, j])
        if board[i][j] == 2:
            virus.append([i, j])
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[0 for _ in range(m)] for _ in range(n)]


def dfs(x, y, visited):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visited[nx][ny] == 1:
            continue
        if board[nx][ny] == 1:
            continue
        visited[nx][ny] = 1
        dfs(nx, ny, visited)


def go(board):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for x, y in virus:
        visited[x][y] = 1
        dfs(x, y, visited)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 and visited[i][j] == 0:
                cnt += 1
    return cnt


l = len(wall)
ret = 0
for i in range(l):
    for j in range(i):
        for k in range(j):
            board[wall[k][0]][wall[k][1]] = 1
            board[wall[j][0]][wall[j][1]] = 1
            board[wall[i][0]][wall[i][1]] = 1
            ret = max(ret, go(board))
            board[wall[k][0]][wall[k][1]] = 0
            board[wall[j][0]][wall[j][1]] = 0
            board[wall[i][0]][wall[i][1]] = 0
print(ret)
