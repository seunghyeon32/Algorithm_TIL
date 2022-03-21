# 1248_공통조상 풀이
# 2022-03-21

import sys
sys.stdin = open('input.txt', 'r')


def preorder(v):
    global cnt
    if v:
        cnt += 1
        preorder(ch1[v])
        preorder(ch2[v])


T = int(input())
for tc in range(1, T+1):
    # V: 트리의 정점의 총 수
    # E: 간선의 총 수
    # n1, n2: 임의의 두 정점
    V, E, n1, n2 = map(int, input().split())
    parents = [0] * (V+1)
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    bridge = list(map(int, input().split()))
    cnt = 0

    # parents: 인덱스를 자식노드번호, 값을 부모노드번호로 하는 리스트
    # ch1, ch2: 인덱스를 부모노드번호, 값을 자식노드번호로 하는 리스트
    for e in range(E):
        n = bridge[2*e]
        val = bridge[2*e+1]
        parents[val] = n
        if not ch1[n]:
            ch1[n] = val
        else:
            ch2[n] = val

    # n1과 n2의 공통 조상 중 가장 가까운 것 찾기
    top1 = list()
    top2 = list()
    while True:
        if n1 != 1:
            top1.append(parents[n1])
            n1 = parents[n1]
            # n1의 조상노드가 n2의 조상노드중에 있다면, root 찾았다 !
            if n1 in top2:
                root = n1
                break
        if n2 != 1:
            top2.append(parents[n2])
            n2 = parents[n2]
            # n2의 조상노드가 n1의 조상노드중에 있다면, root 찾았다 !
            if n2 in top1:
                root = n2
                break

    # 공통 조상노드를 root로 하는 서브트리의 노드 개수 구하기
    preorder(root)
    print('#{} {} {}'.format(tc, root, cnt))
