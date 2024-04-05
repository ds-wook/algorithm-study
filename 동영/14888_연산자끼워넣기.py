"""
N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 
둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 
셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.
"""

# import sys
# from itertools import permutations

# input=sys.stdin.readline
# n=int(input())
# num=list(map(int, input().split()))
# opt=list(map(int, input().split()))
# cal=["+"*opt[0],"-"*opt[1],"*"*opt[2],"/"*opt[3]]

# max_result=-1e9
# min_result=1e9

# for p in set(permutations(cal, n-1)): # 같은 것이 존재함 so set으로 중복 제거
#     result=num[0]

#     for i in range(1,n):
#         if p[i-1] == '+':
#             result += num[i]
#         elif p[i-1] == '-':
#             result -= num[i]
#         elif p[i-1] == '*':
#             result *= num[i]
#         elif p[i-1] == '/':
#             result=int(result/num[i])
    
#     if max_result<result:
#         max_result=result
#     if result<min_result:
#         min_result=result
#     # max_result=max(max_result, result)
#     # min_result=min(min_result, result)
                
# print(max_result)
# print(min_result)


import sys

input=sys.stdin.readline
n=int(input())
num=list(map(int, input().split()))
opt=list(map(int, input().split()))

max_result=-1e9
min_result=1e9

def dfs(depth, total, plus, minus, multi, divide):
    global max_result, min_result
    
    if depth == n:
        max_result = max(total, max_result)
        min_result = min(total, min_result)
        return

    if plus:
        dfs(depth+1, total+num[depth], plus-1, minus, multi, divide)
    if minus:
        dfs(depth+1, total-num[depth], plus, minus-1, multi, divide)
    if multi:
        dfs(depth+1, total*num[depth], plus, minus, multi-1, divide)
    if divide:
        dfs(depth+1, int(total/num[depth]), plus, minus, multi, divide-1)
    

dfs(1, num[0], opt[0], opt[1], opt[2], opt[3])          
print(max_result)
print(min_result)