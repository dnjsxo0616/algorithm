ans = []
score = [list(map(int, input().split())) for _ in range(5)]
for i in score: # 각 인덱스 합을 저장
    ans.append(sum(i))

print(ans.index(max(ans))+1, max(ans))