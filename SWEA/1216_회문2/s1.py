# 1216_회문2 풀이
# 2022-02-17
import sys
sys.stdin = open('input.txt', 'r')
T = 10

for t in range(1, T+1):
    tn = int(input())   # 테스트 케이스 번호
    puzzle = list()     # 문자열 받기
    max_s = 0           # 회문의 최대 길이

    # 상하좌우 쿠션('0') 깔고, 문자열 받기
    puzzle.append('0' * 102)
    for _ in range(100):
        puzzle.append('0' + input() + '0')
    puzzle.append('0' * 102)

    # 회문 찾기
    for i in range(2, 101):
        for j in range(2, 101):
            sr = 0  # 행의 회문길이
            sc = 0  # 열의 회문길이

            # 행에서 찾기
            # 만약 내 양옆의 값이 같으면(홀수길이 회문) ABA
            if puzzle[i][j-1] == puzzle[i][j+1]:
                # 회문의 길이 +3, 양옆으로 넓혀가며 비교
                sr += 3
                nr = 2
                while nr > 1:
                    # 만약 날개들의 값이 또 같으면 반복
                    # CABAC
                    # 다르면, 회문 끝
                    if puzzle[i][j-nr] == puzzle[i][j+nr]:
                        sr += 2
                        nr += 1
                    else:
                        break
                # 구한 회문의 길이가, 최대 회문의 길이보다 길면 바꿔치기 !
                if sr > max_s:
                    max_s = sr

            # 만약 내 오른쪽값과 같으면(짝수길이 회문)
            elif puzzle[i][j] == puzzle[i][j+1]:
                # 회문의 길이 +2
                sr += 2
                nr = 1
                while nr > 0:
                    # j를 기준으로 j+1 == j 이므로
                    # j-nr 과 j+nr+1 비교해서 회문 구하기
                    if puzzle[i][j - nr] == puzzle[i][j + nr + 1]:
                        sr += 2
                        nr += 1
                    else:
                        break
                # 구한 회문의 길이가, 최대 회문의 길이보다 길면 바꿔치기 !
                if sr > max_s:
                    max_s = sr

            # 만약 내 왼쪽값과 같으면(짝수길이 회문)
            elif puzzle[i][j] == puzzle[i][j-1]:
                sr += 2
                nr = 1
                while nr > 0:
                    # j를 기준으로 j-1 == j 이므로
                    # j+nr 과 j-nr-1 비교해서 회문 구하기
                    if puzzle[i][j - nr - 1] == puzzle[i][j + nr]:
                        sr += 2
                        nr += 1
                    else:
                        break
                # 구한 회문의 길이가, 최대 회문의 길이보다 길면 바꿔치기 !
                if sr > max_s:
                    max_s = sr
            else:
                continue

            # 열에서 찾기
            # 행에서 찾는 것과 동일한 방법
            if puzzle[j-1][i] == puzzle[j+1][i]:
                sc += 3
                nc = 2
                while nc > 1:
                    if puzzle[j-nc][i] == puzzle[j+nc][i]:
                        sc += 2
                        nc += 1
                    else:
                        break
                if sc > max_s:
                    max_s = sc

            elif puzzle[j][i] == puzzle[j+1][i]:
                sc += 2
                nc = 1
                while nc > 0:
                    if puzzle[j - nc][i] == puzzle[j + nc + 1][i]:
                        sc += 2
                        nc += 1
                    else:
                        break
                if sc > max_s:
                    max_s = sc

            elif puzzle[j][i] == puzzle[j-1][i]:
                sc += 2
                nc = 1
                while nc > 0:
                    if puzzle[j - nc - 1][i] == puzzle[j + nc][i]:
                        sc += 2
                        nc += 1
                    else:
                        break
                if sc > max_s:
                    max_s = sc
            else:
                continue

    print('#{} {}'.format(tn, max_s))