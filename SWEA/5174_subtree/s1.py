# 5174_subtree 풀이
# 2022-03-17

import sys
sys.stdin = open('sample_input.txt', 'r')


def inorder(v):
    global result

    if v:
        inorder(ch1[v])
        result.append(v)
        inorder(ch2[v])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    graph = list(map(int, input().split()))
    ch1 = [0] * (E+N+1)
    ch2 = [0] * (E+N+1)
    result = list()

    # 부모노드번호를 인덱스로, 자식노드번호 저장
    for e in range(E):
        if not ch1[graph[2*e]]:
            ch1[graph[2*e]] = graph[2*e+1]
        else:
            ch2[graph[2*e]] = graph[2*e+1]

    # N번을 루트노드로 한 중위 탐색
    inorder(N)
    print('#{} {}'.format(tc, len(result)))
