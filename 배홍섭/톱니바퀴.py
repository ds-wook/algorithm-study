# gears = [
#     [1,0,1,0,1,1,1,1],
#     [0,1,1,1,1,1,0,1],
#     [1,1,0,0,1,1,1,0],
#     [0,0,0,0,0,0,1,0],
# ]
# K = 2
# orders = [
#     [3,-1],
#     [1,1]
# ]


# gears = [
# [1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1],
# ]
# K = 3
# orders = [
#     [1, 1],
#     [2, 1],
#     [3, 1],
# ]


# gears = [
#     [1,0,0,0,1,0,1,1],
#     [1,0,0,0,0,0,1,1],
#     [0,1,0,1,1,0,1,1],
#     [0,0,1,1,1,1,0,1],
# ]
# K = 5
# orders = [
#     [1, 1],
#     [2, 1],
#     [3, 1],
#     [4, 1],
#     [1, -1],
# ]


# gears = [
#     [1,0,0,1,0,0,1,1],
#     [0,1,0,1,0,0,1,1],
#     [1,1,1,0,0,0,1,1],
#     [0,1,0,1,0,1,0,1],
# ]
# K = 8
# orders = [
#     [1, 1],
#     [2, 1],
#     [3, 1],
#     [4, 1],
#     [1, -1],
#     [2, -1],
#     [3, -1],
#     [4, -1],
# ]

gears = []
for _ in range(4):
    gears.append(list(map(int, list(input()))))
K = int(input())
orders = []
for _ in range(K):
    orders.append(list(map(int, input().split())))

from collections import defaultdict


def rotation(gear, direction):
    if direction == 1:  # 시계방향
        return [gear[-1]] + gear[:-1]
    elif direction == -1:  # 반시계방향
        return gear[1:] + [gear[0]]
    else:
        raise Exception("Input Wrong direction")


for number, direction in orders:
    dictionary = defaultdict(str)
    for i in range(3):
        left, right = gears[i], gears[i + 1]
        if left[2] == right[6]:
            dictionary[i, i + 1] = "same"
        else:
            dictionary[i, i + 1] = "diff"

    index = number - 1
    if index == 0:  # 첫번째 기어를 돌리는 경우
        gears[index] = rotation(gears[index], direction)
        for i in range(index + 1, 4):
            if dictionary[i - 1, i] == "diff":
                direction = 1 if direction == -1 else -1
                gears[i] = rotation(gears[i], direction)
            else:
                break

    elif index == 3:
        gears[index] = rotation(gears[index], direction)
        for i in range(index - 1, -1, -1):
            if dictionary[i, i + 1] == "diff":
                direction = 1 if direction == -1 else -1
                gears[i] = rotation(gears[i], direction)
            else:
                break
    elif index == 1:
        gears[index] = rotation(gears[index], direction)
        if dictionary[index - 1, index] == "diff":  # 왼쪽 기어 돌리기
            gears[index - 1] = rotation(gears[index - 1], 1 if direction == -1 else -1)

        for i in range(index + 1, 4):  # 오른쪽으로 순차적으로 돌리기
            if dictionary[i - 1, i] == "diff":
                direction = 1 if direction == -1 else -1
                gears[i] = rotation(gears[i], direction)
            else:
                break

    elif index == 2:
        gears[index] = rotation(gears[index], direction)
        if dictionary[index, index + 1] == "diff":  # 오른쪽 기어 돌리기
            gears[index + 1] = rotation(gears[index + 1], 1 if direction == -1 else -1)

        for i in range(index - 1, -1, -1):  # 왼쪽으로 순차적으로 돌리기
            if dictionary[i, i + 1] == "diff":
                direction = 1 if direction == -1 else -1
                gears[i] = rotation(gears[i], direction)
            else:
                break

answer = 0
for i in range(4):
    if gears[i][0] == 0:
        continue

    if i == 0:
        answer += 1
    elif i == 1:
        answer += 2
    elif i == 2:
        answer += 4
    else:
        answer += 8
print(answer)
