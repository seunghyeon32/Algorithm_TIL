# 1945_간단한-소인수분해
# 2022-02-10

import sys

# input.txt 불러오기
# 테스트 케이스
sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    # N: 자연수
    # result: a, b, c, d, e
    # cnt: result의 인덱스
    N = int(input())
    result = [0] * 5
    cnt = 0

    for n in [2, 3, 5, 7, 11]:

        # 자연수 N을 n으로 나눈 나머지가 0 일때, n은 N의 약수
        while N%n == 0:
            result[cnt] += 1
            N = N//n

        cnt += 1

    print('#{} {} {} {} {} {}'.format(tc, result[0], result[1], result[2], result[3], result[4]))
