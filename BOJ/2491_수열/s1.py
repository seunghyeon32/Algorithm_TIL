# 2491_수열 풀이
# 2022-02-27

N = int(input())
nums = list(map(int, input().split()))
max_cnt = 0

for n in range(N):
    cnt = 1
    while n+cnt < N:
        if nums[n+cnt-1] > nums[n+cnt]:
            if max_cnt < cnt:
                max_cnt = cnt
                break
            break
        cnt += 1

    cnt = 1
    while n + cnt < N:
        if nums[n+cnt-1] < nums[n + cnt]:
            if max_cnt < cnt:
                max_cnt = cnt
                break
            break
        cnt += 1

print(max_cnt)

