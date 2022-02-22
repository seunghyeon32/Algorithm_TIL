# 1219_길찾기 풀이
# 2022-02-22

import sys
sys.stdin = open('input.txt', 'r')


# len 함수 구현
def my_len(s):
    c = 0
    for _ in s:
        c += 1
    return c


T = 10  # 테스트 케이스 10개
for t in range(1, T+1):
    # tc: 테스트 케이스 번호, N: 간선의 개수
    # tree: 시작>도착 나열
    # branch: 인덱스 = 출발위치, 값 = 도착위치
    # stack: 스택 초기화
    # top: stack 의 top 인덱스
    # val: stack[top] 값
    # result: 결과
    tc, N = map(int, input().split())
    tree = list(map(int, input().split()))
    branch = [[] for _ in range(100)]
    stack = [0]
    top = 0
    val = 0
    result = 0

    # branch 만들기
    for i in range(0, 2*N, 2):
        branch[tree[i]].append(tree[i+1])

    while stack:
        check = 0      # 스택에 값이 추가되었는지 확인하는 변수

        # 길 찾아가기
        if my_len(branch[val]) > 0:
            top += 1
            stack.append(branch[val].pop(0))
            val = stack[top]
        else:
            # 0에서 다 출발했는데, 더 이상 길이 없으면 못가 !
            if not branch[0]:
                break

            # 길을 못 찾으면, pop !
            stack.pop(top)
            top -= 1

            # 시작으로 돌아오면, 초기화
            if top == -1:
                val = 0
                top = -1
                stack = [0]
            else:
                val = stack[top]

        # 만약 도착하면 찾았다 !
        if val == 99:
            result = 1
            break

    print('#{} {}'.format(tc, result))
