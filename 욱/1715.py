import heapq
from typing import List


def comparis_count_card(cards: List[int]) -> int:
    result = 0

    while len(cards) > 1:
        one = heapq.heappop(cards)
        two = heapq.heappop(cards)
        result += one + two
        heapq.heappush(cards, one + two)

    return result


if __name__ == "__main__":
    n = int(input())
    cards = []
    for _ in range(n):
        heapq.heappush(cards, int(input()))

    print(comparis_count_card(cards))
