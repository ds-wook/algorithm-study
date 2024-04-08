from itertools import combinations
from typing import List, Tuple


def house_chicken(n: int, city: List[List[int]]) -> Tuple[List, List]:
    houses, chickens = [], []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                chickens.append((i, j))

    return houses, chickens


def solve_min_distance(houses: List[Tuple[int, int]], chickens: List[Tuple[int, int]]) -> int:
    min_distance = int(1e9)

    for chicken in combinations(chickens, m):
        distance = 0
        for house in houses:
            chicken_distance = int(1e9)
            for c in chicken:
                chicken_distance = min(chicken_distance, abs(house[0] - c[0]) + abs(house[1] - c[1]))
            distance += chicken_distance

        min_distance = min(min_distance, distance)

    return min_distance


if __name__ == "__main__":
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    houses, chickens = [], []
    houses, chickens = house_chicken(n, city)
    print(solve_min_distance(houses, chickens))
