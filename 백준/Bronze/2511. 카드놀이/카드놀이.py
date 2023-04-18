A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = ''
A_score = 0
B_score = 0
for i in range(10):
    if A[i] > B[i]:
        A_score += 3
        ans = 'A'
    elif A[i] < B[i]:
        B_score += 3
        ans = 'B'
    elif A[i] == B[i]:
        A_score += 1
        B_score += 1
print(A_score, B_score)
if A_score > B_score:
    print('A')
elif A_score < B_score:
    print('B')
else:
    if ans == 'A':
        print('A')
    elif ans == 'B':
        print('B')
    else:
        print('D')