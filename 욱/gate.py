from typing import List


# 특정 원소가 속한 집합을 찾기
def find_parent(parent: List[int], x: int) -> int:
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent: list[int], a: int, b: int) -> None:
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    # 탑승구 게이트 입력
    g = int(input())
    # 비행기의 수 입력
    p = int(input())
    # 부모 테이블 초기화
    parent = [i for i in range(g + 1)]

    result = 0
    for _ in range(p):
        data = find_parent(parent, int(input()))
        if data == 0:
            break

        union_parent(parent, data, data - 1)
        result += 1

    print(result)
