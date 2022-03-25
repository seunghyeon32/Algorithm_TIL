# 1952_수영장 풀이
# 2022-03-25
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    day, month, three_m, year = map(int, input().split())
    check = [0]+list(map(int, input().split()))
    plan = [0] * 13

    for i in range(1, 13):
        plan[i] = plan[i-1] + min(day*check[i], month)

        if i > 2:
            plan[i] = plan[i] if plan[i-3]+three_m >= plan[i] else plan[i-3]+three_m

    plan[12] = year if plan[12] > year else plan[12]

    print('#{} {}'.format(tc, plan[-1]))