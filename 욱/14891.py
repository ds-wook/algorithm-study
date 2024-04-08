def rotation(gear: list, direction: int) -> list:
    if direction == 1:  # 시계방향
        return [gear[-1]] + gear[:-1]
    elif direction == -1:  # 반시계방향
        return gear[1:] + [gear[0]]
    else:
        raise Exception("Input Wrong direction")


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
