# 수의-새로운-연산 풀이
# 2022-03-14

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())
    c1 = 0
    c2 = 0
    r1 = 0
    r2 = 0

    for c in range(1, 142):
        for r in range(1, 142):
            v = c*(c+1)//2 + (c+r-2)*(c+r-1)//2 - c*(c-1)//2
            if v == p:
                c1 = c
                r1 = r
            if v == q:
                c2 = c
                r2 = r
            if c1 != 0 and c2 != 0 and r1 != 0 and r2 != 0:
                break
        if c1 != 0 and c2 != 0 and r1 != 0 and r2 != 0:
            break

    c = c1+c2
    r = r1+r2
    result = c*(c+1)//2 + (c+r-2)*(c+r-1)//2 - c*(c-1)//2
    print('#{} {}'.format(tc, result))