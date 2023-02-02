num = list(map(int, input().split()))
while True:
    if num[0] > num[1]:
        num[0], num[1] = num[1], num[0]
        print(*num)
    if num[1] > num[2]:
        num[1], num[2] = num[2], num[1]
        print(*num)
    if num[2] > num[3]:
        num[2], num[3] = num[3], num[2]
        print(*num)
    if num[3] > num[4]:
        num[3], num[4] = num[4], num[3]
        print(*num)
    if num == [1, 2, 3, 4, 5]:
        break