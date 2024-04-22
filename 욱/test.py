from bisect import bisect_left, bisect_right


def count_value(arr, value: int) -> int:
    left = bisect_left(arr, value)
    right = bisect_right(arr, value)
    return right - left if right - left else -1


if __name__ == "__main__":
    n, x = map(int, input().split())
    array = list(map(int, input().split()))

    count = count_value(array, x)
    print(count)
