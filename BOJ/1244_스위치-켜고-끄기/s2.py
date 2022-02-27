# BOJ_1244_스위치 켜고 끄기
# 2022-02-27

# N: 스위치 개수
# switch: 스위치 상태
# stu_n: 학생 수
N = int(input())
switch = list(map(int, input().split()))
stu_n = int(input())

for _ in range(stu_n):
    # gender: 성별, num: 받은 수
    gender, num = map(int, input().split())
    num = num - 1

    # 남자일 때, 자기가 받은 수의 배수인 스위치의 상태를 바꿈
    if gender == 1:
        for n in range(num, N, num+1):
            switch[n] = int(not(switch[n]))
        continue

    # 여자일 때, 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면
    # 스위치 상태 바꿈
    if gender == 2:
        switch[num] = int(not(switch[num]))
        a = 1

        while 0 <= num-a < N and 0 <= num+a < N:
            if switch[num-a] == switch[num+a]:
                switch[num-a] = switch[num+a] = int(not(switch[num-a]))
            else:
                break
            a += 1

for i in range(0, N, 20):
    print(*switch[i:i+20])
