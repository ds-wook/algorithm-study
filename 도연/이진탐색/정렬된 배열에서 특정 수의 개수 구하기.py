import sys
sys.stdin = open('input.txt','r')
from bisect import bisect_left, bisect_right

N, x = list(map(int, input().split()))
nums = list(map(int, input().split()))

cnt = bisect_right(nums, x) - bisect_left(nums, x)
if cnt==0:
    cnt = -1
print(cnt)