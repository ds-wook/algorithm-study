"""
실패율은 다음과 같이 정의한다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

"""


def solution(N, stages):

    # stages.sort()
    length = len(stages)
    fail = []
    for i in range(1, N + 1):

        cnt = stages.count(i)

        if length == 0:  # 도중에 모든 player가 탈락한 경우
            fail.append((i, 0))
        else:
            fail.append((i, cnt / length))

        length -= cnt

    # print(sorted(fail, key=lambda x:x[1], reverse=True))
    answer = [x[0] for x in sorted(fail, key=lambda x: x[1], reverse=True)]
    return answer
