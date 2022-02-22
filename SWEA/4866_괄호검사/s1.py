# 4866_괄호검사 풀이
# 2022-02-22

import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())


# len 함수 구현
def my_len(i):
    c = 0
    for _ in i:
        c += 1
    return c


for tc in range(1, T+1):
    in_str = input()               # 입력받아오기
    check = [''] * my_len(in_str)  # stack 리스트
    top = -1                       # top 값
    result = 1                     # 결과

    # stack 구현하기
    for s in in_str:
        # open 괄호일 때, append
        if s == '(' or s == '{':
            top += 1
            check[top] = s

        # close 괄호 일때, pop
        if s == ')' or s == '}':
            # 짝이 맞는 경우, 정상동작
            if (s == ')' and check[top] == '(') or (s == '}' and check[top] == '{'):
                check.pop(top)
                top -= 1
            # 짝이 맞지 않는 경우, 잘못된 괄호
            else:
                result = 0
                break

    # check[top]에 값이 남아있는 경우, 결과를 0으로 바꿔줌
    if check[top] != '':
        result = 0

    print('#{} {}'.format(tc, result))