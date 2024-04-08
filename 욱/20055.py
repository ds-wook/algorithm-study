from collections import deque


def solution(belt, robot):
    result = 0
    while True:
        belt.rotate(1)
        robot.rotate(1)
        robot[-1] = 0

        if sum(robot):
            for i in range(n - 2, -1, -1):
                if robot[i] and not robot[i + 1] and belt[i + 1] >= 1:
                    robot[i + 1] = 1
                    robot[i] = 0
                    belt[i + 1] -= 1

            robot[-1] = 0

        if not robot[0] and belt[0] >= 1:
            robot[0] = 1
            belt[0] -= 1

        result += 1

        if belt.count(0) >= k:
            break

    return result


if __name__ == "__main__":
    n, k = map(int, input().split())
    belt = deque(map(int, input().split()))
    robot = deque([0] * n)
    print(solution(belt, robot))
