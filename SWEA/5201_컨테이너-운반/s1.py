# 5201_컨테이너-운반 풀이
# 2022-03-29
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 컨테이너 수, M: 트럭 수
    weights = sorted(list(map(int, input().split())))   # 화물의 무게
    trucks = sorted(list(map(int, input().split())))    # 트럭의 적재용량
    result = 0

    for m in range(M-1, -1, -1):
        for n in range(N-1, -1, -1):
            # 트럭이 운반할 수 있는 무게라면, 운반 !
            if trucks[m] >= weights[n]:
                result += weights.pop(n)
                N -= 1
                break

    print('#{} {}'.format(tc, result))
