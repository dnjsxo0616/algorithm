n = int(input())
for _ in range(n):
    num = list(map(int, input().split()))
    
    num.remove(num[0])
    avg = sum(num)/len(num)
    
    cnt = 0
    for i in num:
        if i > avg:
            cnt += 1
    
    ans = cnt/len(num)*100
    print(f'{ans:.3f}%')