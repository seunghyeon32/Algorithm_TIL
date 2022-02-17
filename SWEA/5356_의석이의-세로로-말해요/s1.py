# 5356_의석이의-세로로-말해요 풀이
# 2022-02-17
import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

# len함수 구현
def length(s):
    cnt = 0
    for _ in s:
        cnt += 1
    return cnt

for tc in range(1, T+1):
    row = list()   # 배열 저장
    max_len = 0    # 제일 긴 행의 길이

    # 배열 받아오기
    for _ in range(5):
        row.append(input())

    # 제일 긴 행의 길이 구하기
    for r in row:
        if max_len < length(r):
            max_len = length(r)

    # 제일 긴 행의 길이에 맞춰 ' ' 추가
    for i in range(5):
        row[i] += ' ' * (max_len - length(row[i]))

    # 세로로 값을 출력하되, ' '인 부분은 생략
    print('#{}'.format(tc), end=' ')
    for n in range(max_len):
        for m in range(5):
            if row[m][n] != ' ':
                print('{}'.format(row[m][n]), end='')
    print()