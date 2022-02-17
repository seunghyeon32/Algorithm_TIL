# 1206_View 풀이
# 2022-02-09

import sys

# 테스트 케이스 = 10회
# input.txt 불러오기
T = 10
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 돌리기
for tc in range(1, T + 1):
    # N: 입력 데이터 개수, nums: 건물높이 리스트
    # val_lst: 조망권을 구하기 위한 리스트, val: 조망권을 구하기 위한 변수
    # result: 결과값을 저장할 변수
    N = int(input())
    nums = list(map(int, input().split()))
    val_lst = [0] * 5
    val = 0
    result = 0

    # x축 양 끝의 2칸은 무시하므로 2에서 N-2까지의 자리에 건물이 존재
    for n in range(2, N-2):
        # x축을 기준으로 -2,-1,+1,+2에 있는 건물들과의 높이 차이 저장
        val_lst[0] = nums[n] - nums[n - 2]
        val_lst[1] = nums[n] - nums[n - 1]
        val_lst[2] = nums[n] - nums[n + 1]
        val_lst[3] = nums[n] - nums[n + 2]

        # 건물이 가장 높은 경우는 255층
        # 즉, 조망권이 가장 좋을 경우로 초기화
        val = 255

        # 양 옆의 4건물 중 조망권은 가장 높은 건물에 의해 결정되므로
        # 조망권이 가장 작은 값이 해당 건물의 조망권이 된다.
        for i in range(4):
            if val >= val_lst[i]:
                val = val_lst[i]

        # 조망권은 음수가 될 수 없음
        if val >= 0:
            result += val

    print('#{} {}'.format(tc, result))