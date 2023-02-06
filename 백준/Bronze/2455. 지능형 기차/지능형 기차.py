ans = []
cnt = 0
for _ in range(4):
    end, start = map(int, input().split())
    cnt = cnt - end + start
    ans.append(cnt)
    # ans 변수에 각 기차의 사람수를 측정해서 가장 큰 수 출력
print(max(ans))