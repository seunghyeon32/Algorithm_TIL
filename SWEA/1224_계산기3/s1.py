# 1224_계산기3 풀이
# 2022-02-24
import sys
sys.stdin = open('input.txt', 'r')

T = 10    # 테스트 케이스 개수
for tc in range(1, T+1):
    N = int(input())   # 문자열의 길이
    calc = input()     # 계산식 문자열
    stack = list()     # 후위표기법으로 변환시 사용될 stack
    out = list()       # 후위표기법으로 표현된 식
    # isp: 스택 연산자 우선순위, icp: in-coming 우선순위
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}

    for c in calc:
        # 숫자일때, out에 append
        if c.isdigit():
            out.append(c)
            continue

        # 스택이 비었을 경우, 스택에 추가
        if not stack:
            stack.append(c)
        else:
            # '('일 경우, 스택에 추가
            if c == '(':
                stack.append(c)

            # ')'일 경우, '('이 나올때까지 stack에서 pop한 후, out에 추가
            elif c == ')':
                while stack[-1] != '(':
                    out.append(stack.pop())
                stack.pop()

            else:
                # stack[-1]의 우선순위가 낮으면 stack에 연산자 추가
                if isp[stack[-1]] < icp[c]:
                    stack.append(c)
                else:
                    # stack[-1]의 우선순위가 낮거나 같은 경우
                    # stack의 top을 out에 추가
                    # stack이 빌 경우, stack에 연산자 추가
                    while isp[stack[-1]] >= icp[c]:
                        out.append(stack.pop())
                        if not stack:
                            stack.append(c)
                            break
                    # stack[-1]의 우선순위가 더 낮으므로 stack에 연산자 추가
                    stack.append(c)

    result_s = list()

    for s in out:
        # 문자면 result_s에 추가
        if s.isdigit():
            result_s.append(int(s))
        else:
            # result_s에 저장된 피연산자 두개를 가져와서 연산을 진행
            b = result_s.pop()
            a = result_s.pop()

            if s == '+':
                result_s.append(b+a)

            if s == '*':
                result_s.append(a*b)


    print('#{} {}'.format(tc, result_s[-1]))

