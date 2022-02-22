# 4873_반복문자-지우기 풀이
# 2022-02-22

import sys
sys.stdin = open('sample_input.txt', 'r')


# len 함수 구현
def my_len(s):
    c = 0
    for _ in s:
        c += 1
    return c


# 테스트 케이스
T = int(input())

for tc in range(1, T + 1):
    in_str = input()                 # 입력값 받아오기
    stack = [''] * my_len(in_str)    # 입력의 크기만큼 문자열 받아오기
    top = -1                         # top 초기화

    for i in in_str:
        # stack[top]과 문자가 같으면, pop하고 top-1
        if stack[top] == i:
            stack.pop(top)
            top -= 1
            continue

        # 기본적으로 top + 1
        # stack[top]에 값 넣어줌
        top += 1
        stack[top] = i

    print('#{} {}'.format(tc, top + 1))
