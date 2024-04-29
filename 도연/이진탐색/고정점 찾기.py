import sys
sys.stdin = open('input.txt','r')

N = int(input())
nums = list(map(int, input().split()))

def binary_search(array, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    # 값이 인덱스와 같으면 인덱스 반환
    if array[mid] == mid:
        return mid
    # 값이 인덱스보다 크면
    elif array[mid] > mid:
        return binary_search(array, start, mid-1)
    # 값이 인덱스보다 작으면
    else:
        return binary_search(array, mid + 1, end)
ans = binary_search(nums, 0, N-1)
print(ans)