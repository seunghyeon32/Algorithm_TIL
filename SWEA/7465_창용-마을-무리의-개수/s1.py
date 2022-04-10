# 7465_창용 마을 무리의 개수
# 2022-04-10

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * (N+1)
    last = 0
    result = 0

    for m in range(M):
        p1, p2 = map(int, input().split())

        # 둘다 무리가 없을 때
        if not visited[p1] and not visited[p2]:
            last += 1
            visited[p1] = last
            visited[p2] = last
            result += 1

        # 둘 중 한명만 무리가 있을 때
        elif not visited[p1]:
            visited[p1] = visited[p2]
        elif not visited[p2]:
            visited[p2] = visited[p1]

        # 둘 다 무리가 있을 때
        else:
            # 같은 무리일 때
            if visited[p1] == visited[p2]:
                continue
            # 서로 다른 무리일 때
            else:
                v = visited[p2]
                for n in range(N+1):
                    if visited[n] == v:
                        visited[n] = visited[p1]
                result -= 1

    result += visited[1:].count(0)
    print('#{} {}'.format(tc, result))