# 5207_이진-탐색 풀이
# 2022-03-31
import sys
sys.stdin = open('sample_input.txt', 'r')


# 재귀로 문제를 해결하면, 깊이가 너무 깊어져서 runtime error 발생 !
def Bin_Search(l, r, i, status):
    global A, B, cnt

    m = (l + r) // 2               # 가운데 인덱스
    if l <= r and B[i] < A[m]:     # 왼쪽 탐색
        if status != 1:            # 이전 탐색이 왼쪽이 아니었다면, 다음 탐색 진행
            return Bin_Search(l, m-1, i, 1)

    elif l <= r and A[m] < B[i]:   # 오른쪽 탐색
        if status != 2:            # 이전 탐색이 오른쪽이 아니었다면, 다음 탐색 진행
            return Bin_Search(m+1, r, i, 2)

    elif B[i] == A[m]:             # 찾았당 !
        cnt += 1
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0

    for m in range(M):
        Bin_Search(0, N-1, m, 0)
    print('#{} {}'.format(tc, cnt))
