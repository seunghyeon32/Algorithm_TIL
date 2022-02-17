# 5432_쇠막대기 풀이
# 2022-02-17
import sys

sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tn in range(1, T + 1):
    cnt = 0                 # 문자열 길이
    laser = input()         # 문자열
    result = 0              # 나눠진 쇠막대기

    # 문자열 길이 계산
    for _ in laser:
        cnt += 1

    cnt_bar = 0   # 쇠막대기 개수
    i = 0         # while 문 제어
    laser += '0'  # 인덱스 에러방지

    while i < cnt:
        # ()나오면 레이저다 !
        # 레이저는 현재있는 쇠막대기 수만큼 조각이 추가됨
        # 따라서 결과에 현재 있는 쇠막대기 개수만큼 더해준다
        # 인덱스 건너뜀
        if laser[i] == '(' and laser[i+1] == ')':
            result += cnt_bar
            i += 2
            continue

        # 레이저가 아닌 )가 있으면, 쇠막대기가 하나 끝난다.
        elif laser[i] == ')':
            cnt_bar -= 1

        # 레이저가 아닌 (가 있으면, 새로운 쇠막대기가 생긴다.
        elif laser[i] == '(':
            cnt_bar += 1
            result += 1
        i += 1

    print('#{} {}'.format(tn, result))

