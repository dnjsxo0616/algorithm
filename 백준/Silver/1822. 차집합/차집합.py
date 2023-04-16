a, b = map(int, input().split())

lis_a = set(map(int,input().split()))
lis_b = set(map(int,input().split()))


# for i in lis_a:
#     if i in lis_b:
#         lis_a.remove(i)
# print(len(lis_a))
# for i in lis_a:
#     print(i, end = ' ')
print(len(lis_a-lis_b))
ans = sorted(list(lis_a-lis_b))
print(*ans)