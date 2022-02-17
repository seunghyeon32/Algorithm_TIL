# 3143_가장-빠른-문자열-타이핑 풀이
# 2022-02-17
import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

# len 함수 구현
def length(s):
    cnt = 0
    for _ in s:
        cnt += 1
    return cnt


for tc in range(1, T+1):
    # A: 타이핑할 문자열, B: 한번에 타이핑 가능한 문자열
    # len_A, len_B: 각 문자열의 길이
    # typing: 타이핑 수
    # n: while문을 제어하는 변수
    A, B = input().split()
    len_A = length(A)
    len_B = length(B)
    typing = 0
    n = 0

    while n < (len_A-len_B+1):
        # 비교할 문자열 초기화
        compare = ''

        # B와 길이가 같은 비교 문자열 만들기
        for i in range(len_B):
            compare += A[n+i]

        # 비교 문자열이 B와 같으면,
        # 1번 타이핑한 후, 타이핑된 문자열을 건너뜀
        if compare == B:
            typing += 1
            n += len_B
            continue
        # 같지 않으면, 한 문자 타이핑 후,
        # 다음 문자열을 생성해 비교
        else:
            typing += 1
            n += 1

    # 한번에 타이핑하는 문자열이 len_A-len_B보다 작을때,
    # 남은 문자열은 한번씩 타이핑해줘야 함.
    typing += (len_A - n)

    print('#{} {}'.format(tc, typing))
