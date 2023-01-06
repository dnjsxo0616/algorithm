# 45분 일찍 알람 설정하기
# 현재 상근이가 설정한 알람 시각이 주어졌을 때
#  (0 ≤ H ≤ 23, 0 ≤ M ≤ 59)
H, M = map(int, input().split())
if M>44:
    print(H, M-45)
elif M<45 and H>0:
    print(H-1,M+15)
else:
    print(23,M+15)
