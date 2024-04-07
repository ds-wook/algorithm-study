def rotation(n: int, d: int) -> None:

    if d == -1:
        tmp_gear = gears[n][0]
        for i in range(7):
            gears[n][i] = gears[n][i + 1]
        gears[n][7] = tmp_gear

    if d == 1:
        tmp_gear = gears[n][7]
        for i in range(7, 0, -1):
            gears[n][i] = gears[n][i - 1]
        gears[n][0] = tmp_gear


def check(n: int, d: int) -> None:
    rs = [(n, d)]

    rdir = -d
    for i in range(n, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            rs.append((i - 1, rdir))
            rdir = -rdir
            continue
        break

    rdir = -d
    for i in range(n, 3):
        if gears[i][2] != gears[i + 1][6]:
            rs.append((i + 1, rdir))
            rdir = -rdir
            continue
        break

    for x, y in rs:
        rotation(x, y)


if __name__ == "__main__":
    gears = [list(map(int, input().strip())) for _ in range(4)]
    k = int(input())

    for _ in range(k):
        n, d = map(int, input().split())
        check(n - 1, d)

    result = sum(2**i for i in range(4) if gears[i][0] == 1)

    print(result)
