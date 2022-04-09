# 5248_그룹-나누기
# 2022-04-09

import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pair = list(map(int, input().split()))
    nums = [0] * (N+1)
    counts = [0] * (N+1)
    last = 0
    
    for m in range(M):
        p1 = pair[2*m]
        p2 = pair[2*m+1]

        if nums[p1] and not nums[p2]:    # p1만 그룹이 존재하는 경우
            nums[p2] = nums[p1]
        elif nums[p2] and not nums[p1]:  # p2만 그룹이 존재하는 경우
            nums[p1] = nums[p2]
        elif nums[p1] and nums[p2]:      # p1, p2가 이미 그룹이 존재하는 경우
            if nums[p1] == nums[p2]:     # 같은 그룹에 존재하면 더 볼 필요 없음 !
                continue
            else:
                num = nums[p2]
                for n in range(1, N+1):  # p2그룹의 번호를 p1으로 다 바꿔줌
                    if nums[n] == num:
                        nums[n] = nums[p1]
                counts[num] = 0  # p2그룹은 없애기 !
        else:
            # 둘다 그룹에 속해있지 않으면
            # 새로운 그룹을 생성해줌 !
            last += 1
            counts[last] = 1
            nums[p1] = last
            nums[p2] = last

    result = counts.count(1)       # 그룹번호가 있으면
    result += nums[1:].count(0)    # 선택받지 못한애들은 혼자 조를 함

    print('#{} {}'.format(tc, result))