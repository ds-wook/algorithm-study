N=3
cards = [10,20,40]

N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))

import heapq

heapq.heapify(cards)

answer=0
while len(cards)>=2:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    answer+=(first+second)
    heapq.heappush(cards, first+second)
    
print(answer)