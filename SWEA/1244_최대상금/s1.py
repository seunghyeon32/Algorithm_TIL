# 15248_부분 직사각형

import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

T = int(input())


def change():
    global num, nums, sorted_nums, check, N

    # 현재 최댓값이 아닌 경우
    if check.count(0):
        maxI = check.index(0)
        maxV = sorted_nums[maxI]

        for i in range(N-1, -1, -1):
            # 이미 자리를 찾은 경우, 교환할 필요 없음
            if check[i]:
                continue

            if nums[i] == maxV:
                if cnt == 1:
                    minI = i
                    break
                else:
                    minI = i

        nums[maxI], nums[minI] = nums[minI], nums[maxI]

        if nums[maxI] == sorted_nums[maxI]:
            check[maxI] = 1

        if nums[minI] == sorted_nums[minI]:
            check[minI] = 1

    # 이미 최댓값인 경우
    else:
        # 같은 수가 있다면 해당 수 끼리 교환하면 되므로, 최댓값이 결과가 됨
        for i in range(N-1):
            if nums[i] == nums[i+1]:
                return

        # 그렇지 않다면, 가장 작은 자리의 숫자끼리 교환
        nums[-1], nums[-2] = nums[-2], nums[-1]


for tc in range(1, T+1):
    num, cnt = map(int, input().split())
    nums = list(map(int, str(num)))
    sorted_nums = sorted(nums, reverse=True)
    check = [0] * (len(nums))
    result = 0
    N = len(nums)

    for n in range(N):
        if nums[n] == sorted_nums[n]:
            check[n] = 1

    # 교환하기
    while cnt > 0:
        change()
        cnt -= 1

    # 결과 변환
    for i in range(N):
        result += nums[i]*10**(N-i-1)

    print(f'#{tc} {result}')