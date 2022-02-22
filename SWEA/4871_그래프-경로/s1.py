# 4871_그래프-경로 풀이
# 2022-02-22

import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())


# len 함수 구현
def my_len(lst):
    c = 0
    for _ in lst:
        c += 1
    return c


for tc in range(1, T + 1):
    # V: 최대 노드 번호, E: 간선의 개수
    # tree: 간선의 경로
    # S: 시작위치, G: 도착위치
    # branch: 인덱스 = 출발위치, 값 = 도착위치
    # stack: 스택 초기화
    # top: 스택의 top 인덱스
    V, E = map(int, input().split())
    tree = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    branch = [[] for _ in range(V + 1)]
    stack = [S]
    top = 0

    # branch 만들기
    # 단방향이므로 0번 인덱스와 찾고자하는 값이 같으면, branch 에 도착 정보 저장
    for i in range(1, V + 1):
        for t in tree:
            if t[0] == i:
                branch[i].append(t.pop(1))

    # 결과 저장
    result = 0

    while stack:
        # 스택에 값이 추가되었는지 확인하는 변수
        check = 0

        # 길 찾기
        for i in range(my_len(branch[S])):
            if branch[S][i] not in stack:
                top += 1
                stack.append(branch[S][i])
                S = branch[S].pop(i)
                check = 1
                break

        # 길을 못찾으면, pop !
        if check == 0:
            stack.pop(top)
            top -= 1
            # 만일 pop한 후 stack이 비면 끝 !
            if top == -1:
                break
            else:
                S = stack[top]

        # 도착하면 찾았다 !
        if stack[top] == G:
            result = 1
            break

    print('#{} {}'.format(tc, result))
