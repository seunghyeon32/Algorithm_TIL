# 2005_파스칼의-삼각형 풀이
# 2022-02-21
import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):

    # 파스칼 삼각형의 크기
    # pascal 초기값
    # out 출력 초기값
    N = int(input())
    pascal = [1]
    out = [1]

    # 1일 때, 출력
    print('#{}'.format(tc))
    print('{}'.format(pascal[0]))

    # 2이상일 때
    for n in range(1, N):
        pascal = list(out)  # 이전 출력값 저장장
        out = [1]           # 출력 초기화
        top = n - 1         # top을 맨 뒤에서 부터

        # 출력 값 구하기
        for m in range(0, n):
            # top이 0이 아닌 경우
           if top > 0:
                # 맨뒤의 값과 그 앞의 값의 합이므로 맨뒤의 값은 한번만 사용
                # 맨뒤의 값을 pop 하였으므로 top - 1
                # out의 맨 뒤 값에 pascal 맨 뒤의 값을 더해줌
                # 여기서는 한 번 더 더해줘야 하기 때문에 pop을 사용하지 않음
                out.append(pascal.pop(top))
                top -= 1
                out[-1] += pascal[top]
            else:
                # 마지막에 pop !
                out.append(pascal.pop(top))

        print(*out)
