# ?가 앞에올경우, ? 뒤에 올경우 두 개 나눠서 생각해야함
from bisect import bisect_left, bisect_right

# 모든 단어를 길이마다 나누어서 저장
array=[[] for _ in range(10001)]
reverse_array=[[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    #words를 길이별로 나눈다.
    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])
    
    for _ in range(10001):
        array[_].sort()
        reverse_array[_].sort()
    
    for query in queries:
        if query[0]=='?':   # ?로 시작 ????o
            # reverse_array[len(query)] = ["emarf","oakak","odorf","tnorf","tsorf"]에서 
            lindex=bisect_left(reverse_array[len(query)], query[::-1].replace('?','a')) # 'oaaaa' 찾기 -> 1
            rindex=bisect_right(reverse_array[len(query)], query[::-1].replace('?','z')) # 'ozzzz' 찾기 -> 3
        else:       # ?로 끝남 fro??
            # array[len(query)] = ["frame","frodo","front","frost","kakao"]
            lindex=bisect_left(array[len(query)], query.replace('?','a')) # 'froaa' 찾기 -> 1
            rindex=bisect_right(array[len(query)], query.replace('?','z')) # 'frozz' 찾기 -> 4
        answer.append(rindex-lindex)
        
    return answer