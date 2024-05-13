import sys
sys.stdin = open('input.txt','r')

N = int(input())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = list(map(int, input().split()))

dp = [0] * (N+1)
for i in range(N-1,-1,-1):  # 뒤에서 앞으로
    if i + T[i] <= N:       # 기간 내 상담 가능
        dp[i] = max(dp[i+1], dp[i + T[i]] + P[i]) # 상담을 안하는게 좋을지 하는게 좋을지
    else:
        dp[i] = dp[i+1]
print(dp[0])