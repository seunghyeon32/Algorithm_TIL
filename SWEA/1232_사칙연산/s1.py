# 1232_사칙연산 풀이
# 2022-03-17

import sys
sys.stdin = open('input.txt', 'r')


def post_order(v):
    global top

    if v:
        post_order(left[v])
        post_order(right[v])
        if type(values[v]) == int:   # 숫자면 nums에 추가
            top += 1
            nums[top] = values[v]
        elif values[v] == '+':       # + 연산
            a = nums[top]
            top -= 1
            nums[top] += a

        elif values[v] == '-':       # - 연산
            a = nums[top]
            top -= 1
            nums[top] -= a

        elif values[v] == '*':       # * 연산
            a = nums[top]
            top -= 1
            nums[top] *= a

        elif values[v] == '/':       # / 연산
            a = nums[top]
            top -= 1
            nums[top] /= a


T = 10
for tc in range(1, T+1):
    N = int(input())          # N: 정점의 수
    values = [0] * (N+1)      # values: 정점의 정보
    left = [0] * (N+1)        # left: 정점의 왼쪽 자식노드번호
    right = [0] * (N+1)       # right: 정점의 오른쪽 자식노드번호
    nums = [0] * (N+1)        # nums: 계산 시, 숫자를 담아둘 리스트
    top = -1                  # nums의 top 정보

    #  TREE 만들기
    for _ in range(N):
        val = list(map(str, input().split()))

        # 정점의 정보가 숫자면 숫자로, 문자면 문자로 저장
        if val[1].isdigit():
            values[int(val[0])] = int(val[1])
        else:
            values[int(val[0])] = val[1]

        # 왼쪽 노드가 있을 때
        if len(val) == 3:
            left[int(val[0])] = int(val[2])

        # 오른쪽 노드가 있을 때
        if len(val) == 4:
            left[int(val[0])] = int(val[2])
            right[int(val[0])] = int(val[3])

    post_order(1)

    # nums에 최종적으로 저장된 결과 출력
    print('#{} {}'.format(tc, int(nums[top])))
