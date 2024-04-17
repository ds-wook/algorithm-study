# 14888번 - 연산자끼워넣기

n = int(input())
nums = list(map(int, input().split()))
op_add, op_sub, op_mul, op_div = map(int, input().split())
min_, max_ = 1000000000, -1000000000
res = 0


def dfs(op_add, op_sub, op_mul, op_div, res, i):
    global max_, min_
    if i == n:
        if res >= max_:
            max_ = res
        if res <= min_:
            min_ = res
        return
    if op_add > 0:
        dfs(op_add - 1, op_sub, op_mul, op_div, res + nums[i], i + 1)
    if op_sub > 0:
        dfs(op_add, op_sub - 1, op_mul, op_div, res - nums[i], i + 1)
    if op_mul > 0:
        dfs(op_add, op_sub, op_mul - 1, op_div, res * nums[i], i + 1)
    if op_div > 0:
        dfs(op_add, op_sub, op_mul, op_div - 1, int(res / nums[i]), i + 1)


dfs(op_add, op_sub, op_mul, op_div, nums[0], 1)
print(max_)
print(min_)
