# 4834_숫자-카드
# 2022-02-10

import sys

# input.txt 불러오기
# 테스트 케이스
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):

    # N: 카드의 장수
    # nums: N개의 숫자들의 리스트
    # counts: 각각의 숫자가 나온 개수를 저장할 리스트 (0~9)
    # many: 가장 많이 나온 횟수, many_n: 가장 많이 나온 숫자
    N = int(input())
    nums = list(map(int, input()))
    counts = [0] * 10
    many = 0
    many_n = 0

    # 숫자들의 개수 저장
    for n in nums:
        counts[n] += 1

    # 가장 많이 나온 횟수와 숫자 찾기
    for i in range(10):
        if many <= counts[i]:
            many = counts[i]
            many_n = i


    print('#{} {} {}'.format(tc, many_n, many))