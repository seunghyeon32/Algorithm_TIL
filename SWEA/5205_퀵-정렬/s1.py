# 5205_퀵-정렬 풀이
# 2022-03-31
import sys
sys.stdin = open('sample_input.txt', 'r')


def QuickSort(nums, l, r):
    if l < r:
        s = partition(nums, l, r)   # 1차 정렬
        QuickSort(nums, l, s-1)     # 나눠진 부분을 기준으로 재정렬
        QuickSort(nums, s+1, r)


def partition(nums, l, r):
    if l >= r:
        return

    pivot = nums[l]     # 피봇값
    i = l + 1           # 피봇의 왼쪽 인덱스부터 탐색
    j = r               # 피봇의 오른쪽 인덱스부터 탐색

    while i <= j:
        # 피봇보다 큰 값이 나올 때까지 i 증가
        while i <= j and nums[i] <= pivot:
            i += 1

        # 피봇보다 작은 값이 나올 때까지 j 감소
        while i <= j and nums[j] >= pivot:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[l], nums[j] = nums[j], nums[l]

    return j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    QuickSort(A, 0, N-1)
    print('#{} {}'.format(tc, A[N//2]))
