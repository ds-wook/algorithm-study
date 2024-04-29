import sys
sys.stdin = open('input.txt','r')

T = int(input())
for _ in range(T):
    n,m = list(map(int, input().split()))
    array = list(map(int, input().split()))
    
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    
    # 다이나믹 프로그래밍 진행
    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i==0:
                left_up = 0 
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i==n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]

            dp[i][j] = dp[i][j] + max(left, left_up, left_down)
    result = 0
    for i in range(n):
        result = max(result, dp[i][-1])
    print(result)
