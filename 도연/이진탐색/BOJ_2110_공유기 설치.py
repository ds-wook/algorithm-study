import sys
sys.stdin = open('input.txt','r')

N, C = list(map(int, input().split()))
home = list(int(input()) for _ in range(N))

home.sort()
# 두 공유기 사이의 거리를 이진탐색 (mid)
start = 1 # 거리 중에 가장 작은 값
end = home[-1] - home[0] # 거리 중에 가장 큰 값
result = 0

while start <= end:
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미
    value = home[0]
    count = 1
    # 현재의 mid값을 이용해 공유기를 설치
    for i in range(1,N):     # 앞에서부터 차근차근 설치
        if home[i] >= value + mid:
            value = home[i]
            count += 1
    if count >= C: # C 개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid        # 최적의 결과를 저장
    else:   # C 개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1
print(result)