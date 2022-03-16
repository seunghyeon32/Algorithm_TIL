# 1231_중위순회 풀이
# 2022-03-16

import sys
sys.stdin = open('input.txt', 'r')


# 중위 순회 구현: L>V>R
def in_order(v):
    global result

    if v:
        in_order(left[v])
        result += value[v]
        in_order(right[v])


T = 10
for tc in range(1, T+1):
    N = int(input())         # N: 정점의 개수
    value = [None] * (N+1)   # value: 각 정점이 가지는 문자
    left = [0] * (N+1)       # left: 부모노드의 번호를 인덱스로 하는 왼쪽자식노드번호
    right = [0] * (N+1)      # right: 오른쪽 자식노드번호
    result = ''              # result: 결과를 저장할 문자열

    for _ in range(N):
        val = list(map(str, input().split()))
        n = int(val[0])      # 노드번호
        value[n] = val[1]    # 노드가 가지는 문자
        left[n] = int(val[2]) if len(val) > 2 else None   # 왼쪽자식노드가 존재할 때, 자식노드 번호 추가
        right[n] = int(val[3]) if len(val) > 3 else None  # 오른쪽자식노드가 존재할 때, 자식노드 번호 추가

    in_order(1)  # 중위순회
    print('#{}'.format(tc), result)