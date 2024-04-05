import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
cnt = list(map(int, sys.stdin.readline().split()))

max_num = -float('inf')
min_num = float('inf')

def dfs(cnt, total, idx):
	global max_num, min_num
	if idx == n:
		max_num = max(max_num, total)
		min_num = min(min_num, total)
		return

	if cnt[0] != 0:
		dfs([cnt[0] - 1] + cnt[1:], total + arr[idx], idx + 1)
	if cnt[1] != 0:
		dfs([cnt[0], cnt[1] - 1] + cnt[2:], total - arr[idx], idx + 1)
	if cnt[2] != 0:
		dfs(cnt[:2] + [cnt[2] - 1] + cnt[3:], total * arr[idx], idx + 1)
	if cnt[3] != 0:
		dfs(cnt[:3] + [cnt[3] - 1], int(total / arr[idx]), idx + 1)

dfs(cnt, arr[0], 1)
print(max_num)
print(min_num)
