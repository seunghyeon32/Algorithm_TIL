# 4875_미로 풀이
# 2022-02-24
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())  # 테스트 케이스 개수
for tc in range(1, T + 1):
    # N: N*N 행렬의 크기
    # maze: N*N 행렬, stack: 경로를 찾아갈 stack
    # result: 결과 값
    # end: 도착점
    # si, sj: 현재위치의 인덱스
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    stack = list()
    result = 0
    end = (N, N)
    si = N
    sj = N

    # 출발점과 도착점 찾기
    for n in range(N):
        for m in range(N):
            # 출발점을 찾아 stack에 넣어줘 !
            if maze[n][m] == 2:
                si = int(n)
                sj = int(m)
                stack.append((n, m))

            # 도착점을 찾아줘 !
            if maze[n][m] == 3:
                end = (n, m)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 상 좌

    while True:
        # 출발점이나 도착점이 존재하지 않을 때, 길이 없어 !
        if sj == N or end[1] == N:
            result = 0
            break

        # 도착점에 도착했을 때, 도착했어 !
        if stack[-1] == end or result == 1:
            result = 1
            break

        find = 0  # 길을 찾았는지 확인할 변수
        cnt = 0   # 출발점에서 움직일 수 있는지 확인할 변수

        # 4방향 탐색
        for d in directions:
            # 출발점에 있을 때, 4방향이 모두 막혔을 경우 cnt = 4
            if maze[si][sj] == 2:
                cnt += 1

            # 인덱스 에러 방지
            if 0 <= si + d[0] < N and 0 <= sj + d[1] < N:
                ci = si + d[0]   # 행의 방향이동
                cj = sj + d[1]   # 열의 방향이동

                # 길이 있을 때, 이동
                if maze[ci][cj] == 0:
                    si = int(ci)            # 현재 행을 바꿔줌
                    sj = int(cj)            # 현재 열을 바꿔줌
                    maze[si][sj] = 1        # 지나간 길을 다시 가지 않도록 막아줌
                    stack.append((si, sj))  # 현재 위치를 stack에 저장
                    find = 1                # 길을 찾았당 !
                    cnt = 0                 # 만일 출발점에 있다면, 길이 있음을 확인
                    break

                # 도착점에 도달했을 경우
                if maze[ci][cj] == 3:
                    find = 1     # 길이 있어 !
                    result = 1   # 도착했어 !
                    cnt = 0      # 만일 출발점에 있다면, 길이 있음을 확인
                    break

        # 출발점에서 더 이상 갈 곳이 없어 !
        # 길이 없으니 끝내줘 !
        if cnt == 4:
            result = 0
            break

        # 나는 출발점도 아니고, 길도 없어 !
        # 되돌아가줘 !
        if cnt != 4 and find == 0 and maze[si][sj] != 2:
            stack.pop()         # 되돌아가 !
            si = stack[-1][0]   # 행의 값도 되돌아가 !
            sj = stack[-1][1]   # 열의 값도 되돌아가 !
            continue

    print('#{} {}'.format(tc, result))
