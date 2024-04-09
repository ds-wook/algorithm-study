'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''

import sys

input=sys.stdin.readline

n,m=list(map(int, input().split()))

def dfs(a, visited):
    if len(a)==m:
        print(" ".join(map(str,a)))
        return

    for i in range(1,n+1):
        if visited[i-1]:
            continue
        visited[i-1]=True
        a.append(i)
        dfs(a, visited)
        a.pop()
        visited[i-1]=False
        
    
dfs([],[False]*n)

###################################### # combination
# from itertools import combinations

# arr=combinations(range(n),m)

# for i in arr:
#     for j in i:
#         print(j+1, end=" ")
#     print()