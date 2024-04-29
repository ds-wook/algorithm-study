def solution(N, stages):
    dic = {key: 0 for key in range(1,N+1)}
    total = len(stages)
    for i in range(1,N+1):
        cnt = stages.count(i)
        dic[i] = cnt / total
        total -= cnt
        if total == 0:
            break
    sort_dic = sorted(dic.items(), key=lambda x: -x[1])
    answer = []
    for k,v in sort_dic:
        answer.append(k)
    return answer