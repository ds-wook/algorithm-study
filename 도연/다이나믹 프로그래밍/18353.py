import sys
sys.stdin = open('input.txt','r')

N = int(input())
ls = list(map(int, input().split()))
# dp = [0] * N
# dp[N-1] = 1
# for i in range(N-2,-1,-1):
#     if ls[i] <= ls[i+1]:
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = dp[i+1] + 1

# 앞쪽에 있는 값이 항상 뒤보다 커야함
# 남아있는 병사 수가 최대가 되어야 함
dp = [1] * N
for i in range(N):
    for j in range(i):
        if ls[i] < ls[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(N - max(dp))