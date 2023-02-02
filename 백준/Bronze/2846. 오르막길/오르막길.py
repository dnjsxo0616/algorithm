n = int(input())

numbers = list(map(int, input().split()))

ans = [numbers[0]]
res = []
for i in numbers:
    if i > ans[-1]:
        ans.append(i)
    elif i <= ans[-1]:
        # ans의 오르막길 크기를 따로 저장한 후 ans를 초기화한 후 i를  넣어준다.
        res.append(ans[-1]-ans[0])
        ans.clear()
        ans.append(i)
res.append(ans[-1]-ans[0])
print(max(res))