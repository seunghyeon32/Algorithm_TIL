# 4874_Forth 풀이
# 2022-02-24
import sys
sys.stdin = open('sample_input.txt', 'r')


# len 함수 구현
def my_len(s):
    c = 0
    for _ in s:
        c += 1
    return c


T = int(input())   # 테스트 케이스의 수

for tc in range(1, T+1):
    in_str = list(map(str, input().split()))   # 후위 표기법 수식
    stack = list()                             # 계산에 이용할 스택

    for n in in_str:
        # n이 숫자일 때, stack에 추가
        if n.isdigit():
            stack.append(int(n))
        # n이 숫자가 아닐 때, 즉 문자일 때
        else:
            # 마침표로 끝나고
            if n == '.':
                # stack의 원소가 하나 남으면, 정상적으로 결과 출력 !
                if my_len(stack) == 1:
                    print('#{} {}'.format(tc, stack.pop()))
                # stack의 원소가 하나 이상이면, 잘못된 수식 !
                else:
                    print('#{} error'.format(tc))
                break

            # 연산자일 때
            else:
                # 피연산자가 2개 이상 존재하지 않으면,
                # 연산이 불가능하므로 잘못된 수식 !
                if my_len(stack) < 2:
                    print('#{} error'.format(tc))
                    break

                # a: 선행하는 피연산자, b: 다음의 피연산자
                b = int(stack.pop())
                a = int(stack.pop())

                # 각 연산자 기호에 따라 계산 후, 결과 값을 stack에 append
                if n == '+':
                    stack.append(a + b)
                elif n == '/':
                    stack.append(a // b)
                elif n == '*':
                    stack.append(a * b)
                elif n == '-':
                    stack.append(a - b)

