# 1226_미로1 풀이
# 2022-03-15


import sys
sys.stdin = open('input.txt', 'r')


def bfs(s):
    global delta
    global arr

    queue = [[s]]

    while queue:
        starts = queue.pop(0)
        v = list()   # 같은 레벨에 있는 값들끼리 담아줌

        for start in starts:  # 한 레벨에서 갈 수 있는 경로를 모두 찾음
            si = start[0]
            sj = start[1]

            for di, dj in delta:
                ci = si + di
                cj = sj + dj

                # 3을 만나면 도착점을 찾았으므로, 함수를 끝내줘 !
                if 0 <= ci < 16 and 0 <= cj < 16 and arr[ci][cj] == 3:
                    return print('#{} {}'.format(tn, 1))

                # 길이 있다면, 경로에 추가해줘 !
                if 0 <= ci < 16 and 0 <= cj < 16 and arr[ci][cj] == 0:
                    v.append([ci, cj])
                    arr[ci][cj] = 1   # 이미 담은 길 표시

        queue.append(v)
        # 더 이상 갈 길이 없다면, 3에 갈 수 없어 !
        if not v:
            return print('#{} {}'.format(tn, 0))


T = 10
for tc in range(1, T+1):
    tn = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
    start_point = [1, 1]
    bfs(start_point)
