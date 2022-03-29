# 5202_화물-도크
# 2022-03-29

import sys
sys.stdin = open('sample_input.txt', 'r')


def best_fit(v, cnt):
    global graph, result

    m = min(graph[v:])   # 가장 최소한의 시간으로 일 할수 있는 위치 구하기
    if m == 24:          # 24시에 일이 끝나는 경우
        result = cnt+1
        return
    elif m == 99:        # 24시 전에 일이 끝나는 경우
        result = cnt
        return
    best_fit(m, cnt+1)   # 일이 끝난 지점부터 다시 탐색 !


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    graph = [99]*25

    # 인덱스 번호에서 갈 수 있는 시간 구하기
    for n in range(N):
        # 만일 갈 곳이 없다면 저장
        if not graph[arr[n][0]]:
            graph[arr[n][0]] = arr[n][1]

        # 동일한 곳이 저장되어 있다면 다음 시간확인
        if arr[n][1] == graph[arr[n][0]]:
            continue

        # 갈 곳이 있지만, 더 빠르게 일을 끝낼 수 있다면 => 빠르게 일을 끝내는 시간으로 바꿔줘 !
        if graph[arr[n][0]] and graph[arr[n][0]] > arr[n][1]:
            graph[arr[n][0]] = arr[n][1]

    result = 0
    best_fit(0, 0)
    print('#{} {}'.format(tc, result))