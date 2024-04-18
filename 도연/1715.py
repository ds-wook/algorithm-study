import heapq

n = int(input())
card = []
for _ in range(n):
    temp = int(input())
    heapq.heappush(card, temp)
# 가장 작은 묶음 두개씩 합치기
# 가장 작은 묶음은 바뀔 수 있음
ans = 0
while len(card)!=1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    ans += a + b
    heapq.heappush(card, a+b)
print(ans)