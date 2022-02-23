# 1223_계산기2 풀이
# 2022-02-23

import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T + 1):
    N = int(input())  # 식의 길이
    calc = input()  # 계산식
    stack = list()  # 스택 초기화
    prior_icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}  # 입력 우선순위
    prior_isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}  # 스택 우선순위
    out = list()    # 후위 표기법 결과

    for i in range(N):
        # 숫자일때는 출력에 append
        if calc[i].isdigit():
            out.append(calc[i])

        else:
            # 스택이 비어있을 때 calc[i] append
            if not stack:
                stack.append(calc[i])

            # 입력의 우선순위가 stack[-1]의 우선순위보다 크면,
            # stack 에 append
            elif prior_icp[calc[i]] > prior_isp[stack[-1]]:
                stack.append(calc[i])
            else:
                while True:
                    # 입력의 우선순위가 stack[-1]의 우선순위보다 작거나 같으면,
                    # stack[-1]을 out 에 append 시킴
                    # 입력의 우선순위보다 stack[-1]의 우선순위가 커졌을 때,
                    # stack 에 append 하고 다음으로 !
                    if prior_icp[calc[i]] <= prior_isp[stack[-1]]:
                        out.append(stack.pop())

                        # 스택이 비면 calc[i]를 append하고 다음으로 !
                        if not stack:
                            stack.append(calc[i])
                            break
                    else:
                        stack.append(calc[i])
                        break

    # 남은 연산자 처리
    while stack:
        out.append(stack.pop())

    # 연산할 스택
    stack_c = list()
    for o in out:
        # 숫자면 스택에 추가
        if o.isdigit():
            stack_c.append(int(o))
        else:
            # 숫자 a, b를 가져옴
            a = stack_c.pop()
            b = stack_c.pop()

            # 더하기 연산자면 a+b를 연산후 stack에 append
            if o == '+':
                stack_c.append(b + a)

            # 곱하기 연산자면 a*b를 연산후 stack에 append
            if o == '*':
                stack_c.append(b * a)

    print('#{} {}'.format(tc, stack_c.pop(0)))
