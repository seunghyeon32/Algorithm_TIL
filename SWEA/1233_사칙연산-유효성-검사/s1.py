# 1233_사칙연산-유효성-검사
# 2022-03-17

import sys
sys.stdin = open('input.txt', 'r')


def postorder(v):
    global top
    global result

    if v:
        postorder(left[v])
        postorder(right[v])

        # 숫자면 calc에 넣어줌
        if type(values[v]) == int:
            top += 1                # 스택에서 후위표기법 연산처럼 숫자를 리스트에 넣어준다고 생각
        else:
            if top == -1:           # 기호가 있는데 더 이상 숫자가 없을 경우
                result = 0          # 0으로 반환
                return
            top -= 1                # 기호를 만나면 숫자하나를 pop해서 연산한다고 생각


for tc in range(1, 11):
    N = int(input())   # 정점의 개수
    values = [None] * 201
    left = [0 for _ in range(201)]
    right = [0 for _ in range(201)]
    top = 0
    result = 1

    for _ in range(N):
        in_str = list(map(str, input().split()))
        # 만일 노드의 값이 숫자면 숫자로, 문자면 문자로 저장
        if in_str[1].isdigit():
            values[int(in_str[0])] = int(in_str[1])
        else:
            values[int(in_str[0])] = in_str[1]

        # 왼쪽 노드가 존재할 때, 저장
        if len(in_str) == 3:
            left[int(in_str[0])] = int(in_str[2])

        # 오른쪽 노드가 존재할 때, 저장
        if len(in_str) == 4:
            left[int(in_str[0])] = int(in_str[2])
            right[int(in_str[0])] = int(in_str[3])

    postorder(1)
    print('#{} {}'.format(tc, result))