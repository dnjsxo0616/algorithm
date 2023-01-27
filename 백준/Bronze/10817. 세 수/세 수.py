a, b, c = list(map(int, input().split()))

# 3개의 수가 모두 다른 경우
if a != b and a != c and b != c:
    if a<b<c or c<b<a:
        print(b)
    elif b<a<c or c<a<b:
        print(a)
    elif a<c<b or b<c<a:
        print(c)
elif a == b or a==c:
    print(a) 
elif b==c:
    print(b)