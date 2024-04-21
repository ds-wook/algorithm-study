def solution(N, stages):
    fail = [0]*(N+1)
    for stage in stages:
        if 0<stage<=N:    fail[stage]+=1
    users = len(stages)
    for idx,fail_number in enumerate(fail):
        try:
            fail[idx]/=users
            users-=fail_number
        except:
            pass
    answer = [[idx,fail_ratio] for idx,fail_ratio in enumerate(fail) if idx!=0]
    answer.sort(key=lambda x:-x[1])
    return [x[0] for x in answer]