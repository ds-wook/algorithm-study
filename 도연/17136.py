import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
paper = [list(map(int, input().split())) for _ in range(10)]
remain = [5, 5, 5, 5, 5]
total = 25


def check(y, x, offset):
    for i in range(y, y + offset + 1):
        for j in range(x, x + offset + 1):
            if paper[i][j] != 1:
                return False
    return True


def backtracking(y, x, c):
    global remain, total
    if y >= 10:
        total = min(total, c)
        return
    if x >= 10:
        backtracking(y + 1, 0, c)
        return
    if paper[y][x] == 1:
        for k in range(5):
            if remain[k] == 0:
                continue
            if y + k >= 10 or x + k >= 10:
                continue

            if not check(y, x, k):
                break
            for i in range(y, y + k + 1):
                for j in range(x, x + k + 1):
                    paper[i][j] = 0
            remain[k] -= 1
            backtracking(y, x + k + 1, c + 1)
            remain[k] += 1
            for i in range(y, y + k + 1):
                for j in range(x, x + k + 1):
                    paper[i][j] = 1
    else:
        backtracking(y, x + 1, c)


backtracking(0, 0, 0)
print(-1 if total == 25 else total)
