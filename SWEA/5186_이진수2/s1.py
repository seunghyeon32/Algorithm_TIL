# 5186_이진수2 풀이
# 2022-03-24
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    a = 1/2        # 계산할 수
    result = ''    # 결과를 저장할 변수

    for i in range(13):
        # 만일 N보다 a가 크거나 같으면 >> '1'
        # 아니면 >> '0'
        if N-a >= 0:
            N = N-a
            result += '1'
        else:
            result += '0'

        # a는 (1/2)만큼 감소하므로 a/2
        a = a/2

        # 변환이 완료되면 멈춤
        if N == 0:
            break

    if N == 0:
        print('#{} {}'.format(tc, result))
    else:
        print('#{} overflow'.format(tc))
