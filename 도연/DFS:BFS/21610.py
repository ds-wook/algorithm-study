import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n,m = map(int, input().split())
basket = [ list(map(int, input().split())) for _ in range(n) ]
magic = [ tuple(map(int, input().split())) for _ in range(m)]

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

# 처음 구름 위치
cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for mag in magic:
    d,s = mag
    moved_cloud = []
    # 구름 이동하고 비 내림
    visited = [[0]*n for _ in range(n)]
    for x,y in cloud:
        nx = (x + dx[d-1] * s) % n
        ny = (y + dy[d-1] * s) % n
        basket[nx][ny] += 1
        moved_cloud.append((nx, ny))
        visited[nx][ny] = 1
    # 대각선의 물 있는 바구니 수만큼 증가
    for r,c in moved_cloud:
        tmp = 0
        for i in [1,3,5,7]:
            if 0 <= r + dx[i] < n and 0 <= c + dy[i] < n and basket[r+dx[i]][c+dy[i]]>0:
                tmp += 1
        basket[r][c] += tmp
    cloud = []
    # 구름 칸을 제외한 나머지 칸 중에서 물의 양이 2 이상인 칸은 물 2 감소
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0 and basket[i][j]>=2:
                basket[i][j] -= 2
                cloud.append((i,j))
# 물의 양 합 계산 후 출력
result = 0
for i in range(n):
    result += sum(basket[i])
print(result)