N = int(input())
ans = 0

for i in range(N):
    a = int(input())
    ans += a
if ans<(N-ans):   
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")