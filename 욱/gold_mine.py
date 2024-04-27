def dynamic_programming():
    max_num = 0
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        dp[i][0] = gold_mine[i][0]

    for i in range(1, m):
        for j in range(n):
            choices = [dp[j][i - 1] + gold_mine[j][i]]
            if j > 0:
                choices.append(dp[j - 1][i - 1] + gold_mine[j][i])
            if j < n - 1:
                choices.append(dp[j + 1][i - 1] + gold_mine[j][i])
            dp[j][i] = max(choices)

    max_num = max(dp[j][m - 1] for j in range(n))

    return max_num


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        data = list(map(int, input().split()))

        gold_mine = [data[i * m : (i + 1) * m] for i in range(n)]
        result = dynamic_programming()
        print(result)
