n = int(input())

ans = []
num = n//4
for i in range(num):
    ans.append('long')

res = ' '.join(ans)
print(f'{res} int')