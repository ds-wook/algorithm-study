import sys
from collections import deque
from typing import List, Tuple


def bfs(x: int, y: int) -> List[Tuple[int]]:
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    union = [(x, y)]

    while q:
        x, y = q.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(country[nx][ny] - country[x][y]) <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    union.append((nx, ny))

    return union


if __name__ == "__main__":
    input = sys.stdin.readline

    n, l, r = map(int, input().split())
    country = [list(map(int, input().split())) for _ in range(n)]

    count = 0

    while True:
        visited = [[False] * n for _ in range(n)]
        move = False

        for x in range(n):
            for y in range(n):
                if not visited[x][y]:
                    union = bfs(x, y)

                    if len(union) > 1:
                        move = True
                        population = sum(country[i][j] for i, j in union) // len(union)

                        for i, j in union:
                            country[i][j] = population

        if not move:
            break

        count += 1

    print(count)
