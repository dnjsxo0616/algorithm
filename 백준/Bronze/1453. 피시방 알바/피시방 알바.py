N = int(input())
num = []
re = []
cus = input().split()
for i in cus:
    if i not in num:
        num.append(i)
    elif i in num:
        re.append(i)
print(len(re))