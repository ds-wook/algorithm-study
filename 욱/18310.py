from typing import List


def solve_min_distance(answer: List[int], n: int) -> int:
    answer.sort()
    return answer[(n - 1) // 2]


if __name__ == "__main__":
    n = int(input())
    answer = list(map(int, input().split()))
    print(solve_min_distance(answer, n))
