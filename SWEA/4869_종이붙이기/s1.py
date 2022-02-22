# 4869_종이붙이기 풀이
# 2022-02-22
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # N: 가로길이 >> 10단위이므로 나눠버림
    # stack: 기본 값 저장
    # top: stack의 top 인덱스
    # num1: 두번째 앞의 값
    N = int(input()) // 10
    stack = [1, 3]
    top = 1
    num1 = stack[0]

    for _ in range(2, N):
        num2 = stack.pop(top)
        top -= 1           # 바로 앞의 값 pop 후, 인덱스 재정비
        stack.append(num2 + 2 * num1)  # 계산의 추가
        num1 = num2        # 다음 계산에서, 바로 앞의 값은 두 번째 앞의 값이 됨
        top += 1           # append 했으므로 top + 1

    print('#{} {}'.format(tc, stack[top]))
