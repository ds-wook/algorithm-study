from typing import List


def install_router(array: List[int], start: int, end: int, c: int) -> None:
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


if __name__ == "__main__":
    n, c = map(int, input().split())
    array = [int(input()) for _ in range(n)]
    array.sort()

    start = 1
    end = array[-1] - array[0]
    answer = 0
    install_router(array, start, end, c)
    print(answer)
