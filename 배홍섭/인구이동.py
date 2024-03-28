N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# N, L, R = 2, 20, 50
# graph = [
#     [50, 30],
#     [20, 40]
# ]

# N,L,R = 2, 40,50
# graph = [
#     [50,30],
#     [20,40]
# ]

# N,L,R = 2, 20, 50
# graph = [
#     [50,30],
#     [30,40]
# ]

# N,L,R = 3, 5, 10
# graph = [
#     [10,15,20],
#     [20,30,25],
#     [40,22,10]
# ]

# N,L,R = 4,10,50
# graph = [
#     [10,100,20,90],
#     [80,100,60,70],
#     [70,20,30,40],
#     [50,20,100,10]
# ]

from collections import defaultdict, deque

count = 0
while True:
    visited = [[False] * N for _ in range(N)]
    no_move = 0
    for row in range(N):
        for column in range(N):
            if not visited[row][column]:
                dq = deque([[row, column]])
                sum_value, visited_regions = 0, []
                while dq:
                    now_row, now_column = dq.popleft()
                    if visited[now_row][now_column]:
                        continue
                    else:
                        visited[now_row][now_column] = True
                        sum_value += graph[now_row][now_column]
                        visited_regions.append([now_row, now_column])

                    if (
                        now_column + 1 < N
                        and L <= abs(graph[now_row][now_column] - graph[now_row][now_column + 1]) <= R
                    ):
                        dq.append([now_row, now_column + 1])

                    if now_row - 1 >= 0 and L <= abs(graph[now_row][now_column] - graph[now_row - 1][now_column]) <= R:
                        dq.append([now_row - 1, now_column])

                    if (
                        now_column - 1 >= 0
                        and L <= abs(graph[now_row][now_column] - graph[now_row][now_column - 1]) <= R
                    ):
                        dq.append([now_row, now_column - 1])

                    if now_row + 1 < N and L <= abs(graph[now_row][now_column] - graph[now_row + 1][now_column]) <= R:
                        dq.append([now_row + 1, now_column])

                if len(visited_regions) == 1:  # 인구이동 불가지역
                    no_move += 1
                    continue

                mean_value = int(sum_value / len(visited_regions))
                for visited_row, visited_column in visited_regions:
                    graph[visited_row][visited_column] = mean_value

    if no_move == N**2:  # 더 이상 인구이동이 일어나지 않는 경우
        break
    else:
        count += 1

print(count)
