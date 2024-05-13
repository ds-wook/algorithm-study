import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n,m = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(n) ]

# 집과 치킨 집의 위치를 먼저 찾기
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append([i,j])
        elif board[i][j] == 2:
            chicken.append([i,j])

visited = [False for _ in range(len(chicken))]
result = 1e9
def dfs(depth, idx):
    global result
    if depth == m:
        ans = 0
        for h in house:
            distance = 1e9
            for j in range(len(chicken)):
                if visited[j]:
                    check = abs(h[0] - chicken[j][0]) + abs(h[1] - chicken[j][1])
                    distance = min(check, distance)
            ans += distance
        result = min(result, ans)
        return
    for k in range(idx, len(chicken)):
        if not visited[k]:
            visited[k] = True
            dfs(depth+1, k+1)
            visited[k] = False
dfs(0, 0)
print(result)