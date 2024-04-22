import sys
from itertools import permutations

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
cnt = list(map(int, sys.stdin.readline().split()))
perm = "+" * cnt[0] + "-" * cnt[1] + "*" * cnt[2] + "/" * cnt[3]
perm_set = set(list(permutations(perm, n - 1)))

max_num = -float("inf")
min_num = float("inf")

for i in perm_set:
    tot = arr[0]
    for j in range(n - 1):
        if i[j] == "+":
            tot += arr[j + 1]
        elif i[j] == "-":
            tot -= arr[j + 1]
        elif i[j] == "*":
            tot *= arr[j + 1]
        elif i[j] == "/":
            if tot < 0:
                tot = -(-tot // arr[j + 1])
            else:
                tot //= arr[j + 1]
    if tot > max_num:
        max_num = tot
    if tot < min_num:
        min_num = tot
print(max_num)
print(min_num)
