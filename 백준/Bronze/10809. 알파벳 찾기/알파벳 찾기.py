import string

S = string.ascii_lowercase # 소문재

n = input()
for i in S:
    print(n.find(i), end = " ")