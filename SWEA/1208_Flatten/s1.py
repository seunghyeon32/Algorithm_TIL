# 1208_Flatten
# 2022-02-10

import sys

# # input.txt 불러오기
# 테스트 케이스
sys.stdin = open('input.txt', 'r')
T = 10

for tc in range(1, T+1):

    # N: 덤프횟수 (1이상 100이하)
    # heights: 상자의 높이들
    # array: 90도 회전했을때 쌓인 상자의 개수
    N = int(input())
    heights = list(map(int, input().split()))
    array = [0] * 100

    # 오른쪽으로 90도 회전했을때, 상자의 높이
    for n in range(100):
        for height in heights:
            if n+1 <= height:
                array[n] += 1


    for m in range(1, 100):
        # 가장 낮은 상자인 경우.
        # 가장 높은 상자를 for문으로 찾는다.
        if array[m] != 100:
            for idx in range(-1, m-100, -1):

                # 가장 높은 상자를 가장 낮은 상자로 dump한다.
                # array[m] 즉, 가장 낮은 상자가 가득차거나, dump 횟수가 끝난 경우
                # 이동을 멈춘다.
                for j in range(array[idx]):
                    if array[m] == 100 or N==0:
                        break
                    array[m] += 1
                    array[idx] -= 1
                    N -= 1

    # 가장 높은 상자와 가장 낮은 상자의 높이를 담을 변수 초기화
    val_1 = 0
    val_2 = 0

    for a in range(100):

        # 가장 낮은 상자 찾기
        if array[a] == 100:
            val_1 = a

        # 가장 높은 상자 찾기
        if array[a] != 100 and array[a] != 0:
            val_2 = a

    # 결과 = 가장 높은 상자 - 가장 낮은 상자
    result = val_2 - val_1

    print('#{} {}'.format(tc, result))
