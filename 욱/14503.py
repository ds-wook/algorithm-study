def clean(x, y, d):
    count = 0

    while True:
        if area[x][y] == 0:
            area[x][y] = -1
            count += 1

        for _ in range(4):
            d = (d - 1) % 4
            nx, ny = x + dx[d], y + dy[d]
            if area[nx][ny] == 0:
                x, y = nx, ny
                break

        else:
            x, y = x - dx[d], y - dy[d]
            if area[x][y] == 1:
                print(count)
                return


if __name__ == "__main__":
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    clean(r, c, d)
