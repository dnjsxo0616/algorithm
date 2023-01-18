N = input()

cnt = 0
new = '' # str

for i in N:
    new = new+i
    if len(new)%10 == 0:
        print(new)
        new = ""
print(new)