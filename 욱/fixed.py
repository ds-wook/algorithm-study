def search_fixed_point(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return -1


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    fixed_point = search_fixed_point(array, 0, n - 1)

    if fixed_point is None:
        print(-1)
    else:
        print(fixed_point)
