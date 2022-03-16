# 1225_암호생성기 풀이
# 2022-02-25

import sys
sys.stdin = open('input.txt', 'r')
T = 10   # 10개의 테스트 케이스
for tc in range(1, T+1):
    # tn: 테스트 케이스 번호
    # nums: 암호를 구할 8개의 숫자
    # stop: 종료조건
    tn = int(input())
    nums = list(map(int, input().split()))
    stop = 0

    while True:
        #
        for i in range(1, 6):
            # nums[0]을 맨뒤로 보낸 후, i만큼 감소 시킨다.
            nums.append(nums.pop(0))
            nums[-1] -= i

            # 종료조건| nums[-1]이 0이거나 음수일때, nums[-1]을 0으로 만들고 멈춘다.
            if nums[-1] <= 0:
                nums[-1] = 0
                stop = 1
                break

        # 암호 생성 완료
        if stop == 1:
            break

    print('#{} '.format(tn), *nums)
