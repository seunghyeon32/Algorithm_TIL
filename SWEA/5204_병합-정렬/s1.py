# 5204_병합-정렬 풀이
# 2022-03-30

import sys
sys.stdin = open('sample_input.txt', 'r')


def mergesort(lst):
    global cnt
    n = len(lst)                # n: 리스트의 길이
    if n <= 1: return           # 리스트의 원소가 하나이면, merge 불가

    # 1. 분할
    mid = n // 2                # mid: 중간 인덱스
    left_group = lst[:mid]      # 왼쪽 리스트
    right_group = lst[mid:]     # 오른쪽 리스트

    mergesort(left_group)       # 왼쪽 mergesort
    mergesort(right_group)      # 오른쪽 mergesort

    l = 0     # left_group 인덱스
    r = 0     # right_group 인덱스
    now = 0   # 바꿔줄 리스트 인덱스

    while l < len(left_group) and r < len(right_group):      # 인덱스 범위 내에서 무한 반복
        if left_group[l] < right_group[r]:      # 왼쪽이 오른쪽보다 작으면
            lst[now] = left_group[l]            # 왼쪽값 넣어줌
            l += 1                              # 다음 왼쪽값 확인
            now += 1                            # 다음 인덱스에 넣어줄거야 !

        else:                                   # 오른쪽이 왼쪽보다 작거나 같으면
            lst[now] = right_group[r]           # 오른쪽 값 넣어줌
            r += 1                              # 다음 오른쪽 값 확인
            now += 1                            # 다음 인덱스에 넣어줄거야 !

    # 왼쪽 값이 남아있으면 다 넣기 !
    while l < len(left_group):
        lst[now] = left_group[l]
        l += 1
        now += 1

    # 오른쪽 값이 남아있으면 다 넣기 !
    while r < len(right_group):
        lst[now] = right_group[r]
        r += 1
        now += 1

    # 왼쪽에서 가장 큰 값이 오른쪽에서 가장 큰 값보다 크면, cnt += 1
    if left_group[-1] > right_group[-1]:
        cnt += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    mergesort(nums)
    print('#{} {} {}'.format(tc, nums[N//2], cnt))
