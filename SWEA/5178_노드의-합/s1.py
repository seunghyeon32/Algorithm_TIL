# 5178_노드의-합 풀이
# 2022-03-21

import sys
sys.stdin = open('sample_input.txt', 'r')


# 자식노드의 합이 부모노드의 값이 됨 >> 후위순회
def postorder(v):
    if not tree[v]:     # 만일 값이 입력 되지 않았다면,
        if v*2 <= N:          # 왼쪽노드
            postorder(v*2)
        if v*2+1 <= N:        # 오른쪽노드
            postorder(v*2+1)

        # 만일 왼쪽노드와 오른쪽 노드가 모두 존재한다면, 두 자식노드의 합이 부모노드의 값
        if v*2 <= N and v*2+1 <= N:
            tree[v] = tree[v*2] + tree[v*2+1]
        # 왼쪽노드만 존재한다면, 왼쪽노드의 값 = 부모노드의 값
        elif v*2 <=N:
            tree[v] = tree[v*2]
        # 왼쪽 노드와 오른쪽 노드가 모두 존재하지 않으면, 같은 레벨의 노드값과 같음
        else:
            tree[v] = tree[v+1]


T = int(input())
for tc in range(1, T+1):
    # N: 노드의 개수, M: 리프노드의 개수, L: 값을 출력할 노드 번호
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    # 리프노드의 값을 저장
    for m in range(M):
        num, val = map(int, input().split())
        tree[num] = val

    postorder(1)
    print('#{} {}'.format(tc, tree[L]))
