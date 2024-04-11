from collections import defaultdict
from typing import List


def solution(N: int, stages: List[int]) -> List[int]:
    users = len(stages)
    failure = defaultdict(int)

    for num in range(1, N + 1):
        try:
            failure[num] = stages.count(num) / users
            users -= stages.count(num)

        except ZeroDivisionError:
            failure[num]

    answer = sorted(failure, key=lambda x: failure[x], reverse=True)

    return answer


if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3, 4, 2, 1, 5])
    print(solution(4, [4, 4, 4, 4]) == [4, 1, 2, 3])
