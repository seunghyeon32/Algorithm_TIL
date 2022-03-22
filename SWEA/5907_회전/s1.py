# 5907_회전 풀이
# 2022-03-22

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # N: 숫자의 개수, M: queue하고 append하는 횟수
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # M번 queue하고 append하는 횟수 = nums의 N%M인덱스의 값
    print('#{} {}'.format(tc, nums[M%N]))