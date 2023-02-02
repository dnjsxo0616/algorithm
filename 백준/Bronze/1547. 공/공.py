cups = ['1', '2', '3']

# 컵의 위치를 바꾼 횟수
M = int(input())

# 횟수 반복
for i in range(M):
    # 바꾼 컵의 번호 두 개 입력
    ch1, ch2 = input().split() # 1 2
    a = cups.index(ch1)
    b = cups.index(ch2)
    cups[a] , cups[b] = ch2,  ch1

# 공의 위치 문자 1의 위치를 출력 리스트 인덱스 0 출력 처음
print(cups[0])