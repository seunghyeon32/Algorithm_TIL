# 4828_min-max
# 2022-02-10

import sys

# input.txt 불러오기
# 테스트 케이스
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

# 테스트 케이스 돌리기
for tc in range(1, T+1):

    # N: 숫자의 개수
    # nums: 숫자들의 리스트
    # max_n, min_n: 최솟값과 최댓값을 저장할 변수 초기화
    N = int(input())
    nums = list(map(int, input().split()))
    max_n = 1
    min_n = 1000000

    for n in nums:
        # 최댓값 구하기
        if n >= max_n:
            max_n = n

        # 최솟값 구하기
        if n <= min_n:
            min_n = n

    print('#{} {}'.format(tc, max_n-min_n))
