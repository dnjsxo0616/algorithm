n = input()
cntl = 0
cntr = 0

for i in n:
    if i == "@":
        cntl +=1
    elif i == "(":
        break

ns = reversed(n)
for j in ns:
    if j == "@":
        cntr += 1
    elif j == ")":
        break

print(cntl, cntr)