n = int(input())
num = list(map(int, input().split()))

num_max= max(num)

cnt = 0
for i in num:
    cnt += (i/num_max*100)
print(cnt/n)