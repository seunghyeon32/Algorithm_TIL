# 1234_비밀번호 풀이
# 2022-02-22

import sys
sys.stdin = open('input.txt', 'r')
T = 10

for tc in range(1, T+1):
    N, secret = map(str, input().split())  # N: 문자열 길이, secret: 비밀번호가 숨어 있는 문자열
    N = int(N)
    stack = [secret[0]]    # 비밀번호를 만들 리스트

    for i in range(1, N):
        # stack 비어있을 경우, secret[i] 추가
        # stack이 비어있지 않을 경우,
        # stack[top]과 secret[i]가 같은 경우, pop
        if stack != [] and stack[-1] == secret[i]:
            stack.pop()
        else:
            stack.append(secret[i])

    print('#{} {} '.format(tc, ''.join(stack)))
