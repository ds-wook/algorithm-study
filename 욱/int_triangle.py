def solution(triangle):
    floor = len(triangle)

    while floor > 0:
        for i in range(floor - 1):
            triangle[floor - 2][i] += max(triangle[floor - 1][i], triangle[floor - 1][i + 1])
        floor -= 1

    return triangle[0][0]


if __name__ == "__main__":
    result = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
    print(result)  # Expect 30
