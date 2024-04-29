n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
for i in range(n-1,0,-1):
    for j in range(i):
        ls[i-1][j] += max(ls[i][j], ls[i][j+1])
print(ls[0][0])