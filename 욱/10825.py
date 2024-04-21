import sys
from typing import List


def sort_key(students: List[List[str]]) -> List[List[str]]:
    return sorted(students, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    students = [input().split() for _ in range(n)]
    students = sort_key(students)

    print("\n".join(map(lambda x: x[0], students)))
