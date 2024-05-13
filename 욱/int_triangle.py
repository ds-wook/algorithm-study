def solution(triangle):
    dp = triangle.copy()
    depth = len(dp)

    for i in range(1, depth):
        for j in range(i + 1):
            print(dp)
            if j == 0:
                dp[i][j] += dp[i - 1][j]
            elif j == i:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

    return max(dp[depth - 1])


if __name__ == "__main__":
    result = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
    print(result)  # Expect 30
