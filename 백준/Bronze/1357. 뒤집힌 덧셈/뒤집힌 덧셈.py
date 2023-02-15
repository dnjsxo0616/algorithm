def Rev(a):
    b = str(a)[::-1]
    return int(b)


x, y = map(int, input().split())
print(Rev(Rev(x)+Rev(y)))