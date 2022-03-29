# 5202_화물-도크
# 2022-03-29

import sys
sys.stdin = open('sample_input.txt', 'r')


def combi(n, picked, topick):
    global result

    if topick == 0:
        c = 1
        for l in range(len(picked) - 1):
            if arr[picked[l]][1] <= arr[picked[l + 1]][0]:
                c += 1
                continue
            else:
                break

        if c > result:
            result = c
        return

    small = 0 if not picked else picked[-1]
    for i in range(small, n):
        if i not in picked:
            combi(n, picked+[i], topick-1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(i, N):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    for n in range(N, 0, -1):
        combi(N, [], n)
        if result == n:
            break

    print('#{} {}'.format(tc, result))
