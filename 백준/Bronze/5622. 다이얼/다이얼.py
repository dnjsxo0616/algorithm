import sys
input = sys.stdin.readline

diary = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

string = input()
time = 0

for i in string:
    for j in diary:
        if i in j:
            time += diary.index(j) + 3
print(time)