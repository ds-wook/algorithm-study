N = int(input())
loc = list(map(int, input().split()))
loc.sort()
# 중앙값
print(loc[(N-1)//2])