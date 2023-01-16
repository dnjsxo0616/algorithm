N = int(input())
ans = []
o = 0
x = 0

for i in range(N):
    a = int(input())
    ans.append(a)

for j in ans:
    if j == 1:
        o += 1
    elif j == 0:
        x +=1

if o>x:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")